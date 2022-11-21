# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._exposure_control_operations import (
    build_get_feature_value_by_factory_request,
    build_get_feature_value_request,
    build_query_feature_values_by_factory_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ExposureControlOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datafactory.aio.DataFactoryManagementClient`'s
        :attr:`exposure_control` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def get_feature_value(
        self,
        location_id: str,
        exposure_control_request: _models.ExposureControlRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific location.

        :param location_id: The location identifier. Required.
        :type location_id: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_feature_value(
        self, location_id: str, exposure_control_request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific location.

        :param location_id: The location identifier. Required.
        :type location_id: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def get_feature_value(
        self, location_id: str, exposure_control_request: Union[_models.ExposureControlRequest, IO], **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific location.

        :param location_id: The location identifier. Required.
        :type location_id: str
        :param exposure_control_request: The exposure control request. Is either a model type or a IO
         type. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ExposureControlResponse]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(exposure_control_request, (IO, bytes)):
            _content = exposure_control_request
        else:
            _json = self._serialize.body(exposure_control_request, "ExposureControlRequest")

        request = build_get_feature_value_request(
            location_id=location_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.get_feature_value.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExposureControlResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_feature_value.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/getFeatureValue"}  # type: ignore

    @overload
    async def get_feature_value_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_request: _models.ExposureControlRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_feature_value_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_request: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def get_feature_value_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_request: Union[_models.ExposureControlRequest, IO],
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_request: The exposure control request. Is either a model type or a IO
         type. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ExposureControlResponse]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(exposure_control_request, (IO, bytes)):
            _content = exposure_control_request
        else:
            _json = self._serialize.body(exposure_control_request, "ExposureControlRequest")

        request = build_get_feature_value_by_factory_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.get_feature_value_by_factory.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExposureControlResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_feature_value_by_factory.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getFeatureValue"}  # type: ignore

    @overload
    async def query_feature_values_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_batch_request: _models.ExposureControlBatchRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlBatchResponse:
        """Get list of exposure control features for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_batch_request: The exposure control request for list of features.
         Required.
        :type exposure_control_batch_request:
         ~azure.mgmt.datafactory.models.ExposureControlBatchRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlBatchResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlBatchResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def query_feature_values_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_batch_request: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlBatchResponse:
        """Get list of exposure control features for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_batch_request: The exposure control request for list of features.
         Required.
        :type exposure_control_batch_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlBatchResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlBatchResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def query_feature_values_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_batch_request: Union[_models.ExposureControlBatchRequest, IO],
        **kwargs: Any
    ) -> _models.ExposureControlBatchResponse:
        """Get list of exposure control features for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_batch_request: The exposure control request for list of features. Is
         either a model type or a IO type. Required.
        :type exposure_control_batch_request:
         ~azure.mgmt.datafactory.models.ExposureControlBatchRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlBatchResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlBatchResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ExposureControlBatchResponse]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(exposure_control_batch_request, (IO, bytes)):
            _content = exposure_control_batch_request
        else:
            _json = self._serialize.body(exposure_control_batch_request, "ExposureControlBatchRequest")

        request = build_query_feature_values_by_factory_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.query_feature_values_by_factory.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExposureControlBatchResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_feature_values_by_factory.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryFeaturesValue"}  # type: ignore
