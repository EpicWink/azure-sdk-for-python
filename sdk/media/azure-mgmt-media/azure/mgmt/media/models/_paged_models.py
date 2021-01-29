# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class AccountFilterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AccountFilter <azure.mgmt.media.models.AccountFilter>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AccountFilter]'}
    }

    def __init__(self, *args, **kwargs):

        super(AccountFilterPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.media.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class MediaServicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`MediaService <azure.mgmt.media.models.MediaService>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[MediaService]'}
    }

    def __init__(self, *args, **kwargs):

        super(MediaServicePaged, self).__init__(*args, **kwargs)
class AssetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Asset <azure.mgmt.media.models.Asset>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Asset]'}
    }

    def __init__(self, *args, **kwargs):

        super(AssetPaged, self).__init__(*args, **kwargs)
class AssetFilterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AssetFilter <azure.mgmt.media.models.AssetFilter>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AssetFilter]'}
    }

    def __init__(self, *args, **kwargs):

        super(AssetFilterPaged, self).__init__(*args, **kwargs)
class ContentKeyPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ContentKeyPolicy <azure.mgmt.media.models.ContentKeyPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ContentKeyPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ContentKeyPolicyPaged, self).__init__(*args, **kwargs)
class TransformPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Transform <azure.mgmt.media.models.Transform>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Transform]'}
    }

    def __init__(self, *args, **kwargs):

        super(TransformPaged, self).__init__(*args, **kwargs)
class JobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Job <azure.mgmt.media.models.Job>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Job]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobPaged, self).__init__(*args, **kwargs)
class StreamingPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StreamingPolicy <azure.mgmt.media.models.StreamingPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StreamingPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(StreamingPolicyPaged, self).__init__(*args, **kwargs)
class StreamingLocatorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StreamingLocator <azure.mgmt.media.models.StreamingLocator>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StreamingLocator]'}
    }

    def __init__(self, *args, **kwargs):

        super(StreamingLocatorPaged, self).__init__(*args, **kwargs)
class LiveEventPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LiveEvent <azure.mgmt.media.models.LiveEvent>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LiveEvent]'}
    }

    def __init__(self, *args, **kwargs):

        super(LiveEventPaged, self).__init__(*args, **kwargs)
class LiveOutputPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LiveOutput <azure.mgmt.media.models.LiveOutput>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LiveOutput]'}
    }

    def __init__(self, *args, **kwargs):

        super(LiveOutputPaged, self).__init__(*args, **kwargs)
class StreamingEndpointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StreamingEndpoint <azure.mgmt.media.models.StreamingEndpoint>` object
    """

    _attribute_map = {
        'next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StreamingEndpoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(StreamingEndpointPaged, self).__init__(*args, **kwargs)