# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import logging
import os
from typing import TYPE_CHECKING

from .chained import ChainedTokenCredential
from .environment import EnvironmentCredential
from .managed_identity import ManagedIdentityCredential
from .._constants import EnvironmentVariables
from .._internal import get_default_authority, normalize_authority

if TYPE_CHECKING:
    # pylint:disable=unused-import,ungrouped-imports
    from typing import Any
    from azure.core.credentials import AccessToken

_LOGGER = logging.getLogger(__name__)


class AzureApplicationCredential(ChainedTokenCredential):
    """A credential for Azure Active Directory applications.

    This credential is designed for applications deployed to Azure (:class:`~azure.identity.DefaultAzureCredential` is
    better suited to local development). It authenticates service principals and managed identities.

    For service principal authentication, set these environment variables to identify a principal:

        - **AZURE_TENANT_ID**: ID of the service principal's tenant. Also called its "directory" ID.
        - **AZURE_CLIENT_ID**: the service principal's client ID

    And one of these to authenticate that principal:

        - **AZURE_CLIENT_SECRET**: one of the service principal's client secrets

        **or**

        - **AZURE_CLIENT_CERTIFICATE_PATH**: path to a PEM-encoded certificate file including the private key. The
          certificate must not be password-protected.

    See `Azure CLI documentation <https://docs.microsoft.com/cli/azure/create-an-azure-service-principal-azure-cli>`_
    for more information about creating and managing service principals.

    When this environment configuration is incomplete, the credential will attempt to authenticate a managed identity.
    See `Azure Active Directory documentation
    <https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview>`_ for an overview of
    managed identities.

    :keyword bool allow_multitenant_authentication: when True, enables the credential to acquire tokens from any tenant
        the application or user is registered in. When False, which is the default, the credential will acquire tokens
        only from the tenant specified by **AZURE_TENANT_ID**. This argument doesn't apply to managed identity
        authentication.
    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud, which is the default when no value is given for this keyword argument or
        environment variable AZURE_AUTHORITY_HOST. :class:`~azure.identity.AzureAuthorityHosts` defines authorities for
        other clouds. Authority configuration applies only to service principal authentication.
    :keyword str managed_identity_client_id: The client ID of a user-assigned managed identity. Defaults to the value
        of the environment variable AZURE_CLIENT_ID, if any. If not specified, a system-assigned identity will be used.
    """

    def __init__(self, **kwargs):
        # type: (**Any) -> None
        authority = kwargs.pop("authority", None)
        authority = normalize_authority(authority) if authority else get_default_authority()
        managed_identity_client_id = kwargs.pop(
            "managed_identity_client_id", os.environ.get(EnvironmentVariables.AZURE_CLIENT_ID)
        )
        super(AzureApplicationCredential, self).__init__(
            EnvironmentCredential(authority=authority, **kwargs),
            ManagedIdentityCredential(client_id=managed_identity_client_id, **kwargs),
        )

    def get_token(self, *scopes, **kwargs):
        # type: (*str, **Any) -> AccessToken
        """Request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The exception has a
            `message` attribute listing each authentication attempt and its error message.
        """
        if self._successful_credential:
            token = self._successful_credential.get_token(*scopes, **kwargs)
            _LOGGER.info(
                "%s acquired a token from %s", self.__class__.__name__, self._successful_credential.__class__.__name__
            )
            return token

        return super(AzureApplicationCredential, self).get_token(*scopes, **kwargs)
