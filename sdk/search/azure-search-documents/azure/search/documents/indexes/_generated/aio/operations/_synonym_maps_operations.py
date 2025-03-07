# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ...operations._synonym_maps_operations import build_create_or_update_request, build_create_request, build_delete_request, build_get_request, build_list_request

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SynonymMapsOperations:
    """SynonymMapsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.search.documents.indexes.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create_or_update(
        self,
        synonym_map_name: str,
        synonym_map: "_models.SynonymMap",
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.SynonymMap":
        """Creates a new synonym map or updates a synonym map if it already exists.

        :param synonym_map_name: The name of the synonym map to create or update.
        :type synonym_map_name: str
        :param synonym_map: The definition of the synonym map to create or update.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SynonymMap"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        json = self._serialize.body(synonym_map, 'SynonymMap')

        request = build_create_or_update_request(
            synonym_map_name=synonym_map_name,
            content_type=content_type,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            json=json,
            template_url=self.create_or_update.metadata['url'],
        )._to_pipeline_transport_request()
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('SynonymMap', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('SynonymMap', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/synonymmaps(\'{synonymMapName}\')'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        synonym_map_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a synonym map.

        :param synonym_map_name: The name of the synonym map to delete.
        :type synonym_map_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_delete_request(
            synonym_map_name=synonym_map_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            template_url=self.delete.metadata['url'],
        )._to_pipeline_transport_request()
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/synonymmaps(\'{synonymMapName}\')'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        synonym_map_name: str,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.SynonymMap":
        """Retrieves a synonym map definition.

        :param synonym_map_name: The name of the synonym map to retrieve.
        :type synonym_map_name: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SynonymMap"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_get_request(
            synonym_map_name=synonym_map_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.get.metadata['url'],
        )._to_pipeline_transport_request()
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SynonymMap', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/synonymmaps(\'{synonymMapName}\')'}  # type: ignore


    @distributed_trace_async
    async def list(
        self,
        select: Optional[str] = None,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.ListSynonymMapsResult":
        """Lists all synonym maps available for a search service.

        :param select: Selects which top-level properties of the synonym maps to retrieve. Specified as
         a comma-separated list of JSON property names, or '*' for all properties. The default is all
         properties.
        :type select: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListSynonymMapsResult, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.ListSynonymMapsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListSynonymMapsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_list_request(
            select=select,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.list.metadata['url'],
        )._to_pipeline_transport_request()
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ListSynonymMapsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': '/synonymmaps'}  # type: ignore


    @distributed_trace_async
    async def create(
        self,
        synonym_map: "_models.SynonymMap",
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.SynonymMap":
        """Creates a new synonym map.

        :param synonym_map: The definition of the synonym map to create.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SynonymMap"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        json = self._serialize.body(synonym_map, 'SynonymMap')

        request = build_create_request(
            content_type=content_type,
            x_ms_client_request_id=_x_ms_client_request_id,
            json=json,
            template_url=self.create.metadata['url'],
        )._to_pipeline_transport_request()
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SynonymMap', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/synonymmaps'}  # type: ignore

