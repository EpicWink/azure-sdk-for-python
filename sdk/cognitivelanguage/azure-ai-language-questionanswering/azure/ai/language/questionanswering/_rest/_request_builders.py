# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_query_knowledge_base_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Answers the specified question using your knowledge base.

    Answers the specified question using your knowledge base.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword project_name: The name of the project to use.
    :paramtype project_name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Post body of the request.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Post body of the request.
    :paramtype content: any
    :keyword deployment_name: The name of the specific deployment of the project to use.
    :paramtype deployment_name: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "answerSpanRequest": {
                    "confidenceScoreThreshold": "float (optional)",
                    "enable": "bool (optional)",
                    "topAnswersWithSpan": "int (optional)"
                },
                "confidenceScoreThreshold": "float (optional)",
                "context": {
                    "previousQnaId": "int",
                    "previousUserQuery": "str (optional)"
                },
                "includeUnstructuredSources": "bool (optional)",
                "qnaId": "int (optional)",
                "question": "str (optional)",
                "rankerType": "str (optional)",
                "strictFilters": {
                    "compoundOperation": "str (optional)",
                    "metadataFilter": {
                        "compoundOperation": "str (optional)",
                        "metadata": {
                            "str": "str (optional)"
                        }
                    },
                    "sourceFilter": [
                        "str (optional)"
                    ]
                },
                "top": "int (optional)",
                "userId": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "answers": [
                    {
                        "answer": "str (optional)",
                        "answerSpan": {
                            "confidenceScore": "float (optional)",
                            "length": "int (optional)",
                            "offset": "int (optional)",
                            "text": "str (optional)"
                        },
                        "confidenceScore": "float (optional)",
                        "dialog": {
                            "isContextOnly": "bool (optional)",
                            "prompts": [
                                {
                                    "displayOrder": "int (optional)",
                                    "displayText": "str (optional)",
                                    "qnaId": "int (optional)"
                                }
                            ]
                        },
                        "id": "int (optional)",
                        "metadata": {
                            "str": "str (optional)"
                        },
                        "questions": [
                            "str (optional)"
                        ],
                        "source": "str (optional)"
                    }
                ]
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    project_name = kwargs.pop('project_name')  # type: str
    deployment_name = kwargs.pop('deployment_name', None)  # type: Optional[str]

    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/:query-knowledgebases')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['projectName'] = _SERIALIZER.query("project_name", project_name, 'str')
    if deployment_name is not None:
        query_parameters['deploymentName'] = _SERIALIZER.query("deployment_name", deployment_name, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_query_text_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Answers the specified question using the provided text in the body.

    Answers the specified question using the provided text in the body.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Post body of the request.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Post body of the request.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "language": "str (optional)",
                "question": "str",
                "records": [
                    {
                        "id": "str",
                        "text": "str"
                    }
                ],
                "stringIndexType": "str (optional). Default value is \"TextElements_v8\""
            }

            # response body for status code(s): 200
            response.json() == {
                "answers": [
                    {
                        "answer": "str (optional)",
                        "answerSpan": {
                            "confidenceScore": "float (optional)",
                            "length": "int (optional)",
                            "offset": "int (optional)",
                            "text": "str (optional)"
                        },
                        "confidenceScore": "float (optional)",
                        "id": "str (optional)",
                        "length": "int (optional)",
                        "offset": "int (optional)"
                    }
                ]
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-05-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/:query-text')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )
