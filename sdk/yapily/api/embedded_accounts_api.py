# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.157.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient
from yapily.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EmbeddedAccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def initiate_embedded_account_request_using_post(self, account_auth_request, **kwargs):  # noqa: E501
        """Initiate a new embedded account request for user to authorize  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_embedded_account_request_using_post(account_auth_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AccountEmbeddedAuthorisationRequest account_auth_request: accountAuthRequest (required)
        :param str x_yapily_api_version: __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0`
        :param str psu_id: __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_corporate_id: __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_ip_address: __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfAuthorisationEmbeddedRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.initiate_embedded_account_request_using_post_with_http_info(account_auth_request, **kwargs)  # noqa: E501

    def initiate_embedded_account_request_using_post_with_http_info(self, account_auth_request, **kwargs):  # noqa: E501
        """Initiate a new embedded account request for user to authorize  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_embedded_account_request_using_post_with_http_info(account_auth_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AccountEmbeddedAuthorisationRequest account_auth_request: accountAuthRequest (required)
        :param str x_yapily_api_version: __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0`
        :param str psu_id: __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_corporate_id: __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_ip_address: __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfAuthorisationEmbeddedRequestResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_auth_request',
            'x_yapily_api_version',
            'psu_id',
            'psu_corporate_id',
            'psu_ip_address'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initiate_embedded_account_request_using_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_auth_request' is set
        if self.api_client.client_side_validation and ('account_auth_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_auth_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_auth_request` when calling `initiate_embedded_account_request_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_yapily_api_version' in local_var_params:
            header_params['x-yapily-api-version'] = local_var_params['x_yapily_api_version']  # noqa: E501
        if 'psu_id' in local_var_params:
            header_params['psu-id'] = local_var_params['psu_id']  # noqa: E501
        if 'psu_corporate_id' in local_var_params:
            header_params['psu-corporate-id'] = local_var_params['psu_corporate_id']  # noqa: E501
        if 'psu_ip_address' in local_var_params:
            header_params['psu-ip-address'] = local_var_params['psu_ip_address']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_auth_request' in local_var_params:
            body_params = local_var_params['account_auth_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/embedded-account-auth-requests', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfAuthorisationEmbeddedRequestResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_embedded_account_request_using_put(self, consent_id, account_auth_request, **kwargs):  # noqa: E501
        """Update an embedded account request with SCA info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_embedded_account_request_using_put(consent_id, account_auth_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent_id: __Mandatory__. The consent Id of the `Consent` to update. (required)
        :param AccountEmbeddedAuthorisationRequest account_auth_request: accountAuthRequest (required)
        :param str x_yapily_api_version: __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0`
        :param str psu_id: __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_corporate_id: __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_ip_address: __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfAuthorisationEmbeddedRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_embedded_account_request_using_put_with_http_info(consent_id, account_auth_request, **kwargs)  # noqa: E501

    def update_embedded_account_request_using_put_with_http_info(self, consent_id, account_auth_request, **kwargs):  # noqa: E501
        """Update an embedded account request with SCA info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_embedded_account_request_using_put_with_http_info(consent_id, account_auth_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent_id: __Mandatory__. The consent Id of the `Consent` to update. (required)
        :param AccountEmbeddedAuthorisationRequest account_auth_request: accountAuthRequest (required)
        :param str x_yapily_api_version: __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0`
        :param str psu_id: __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_corporate_id: __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_ip_address: __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfAuthorisationEmbeddedRequestResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'consent_id',
            'account_auth_request',
            'x_yapily_api_version',
            'psu_id',
            'psu_corporate_id',
            'psu_ip_address'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_embedded_account_request_using_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consent_id' is set
        if self.api_client.client_side_validation and ('consent_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent_id` when calling `update_embedded_account_request_using_put`")  # noqa: E501
        # verify the required parameter 'account_auth_request' is set
        if self.api_client.client_side_validation and ('account_auth_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_auth_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_auth_request` when calling `update_embedded_account_request_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in local_var_params:
            path_params['consentId'] = local_var_params['consent_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_yapily_api_version' in local_var_params:
            header_params['x-yapily-api-version'] = local_var_params['x_yapily_api_version']  # noqa: E501
        if 'psu_id' in local_var_params:
            header_params['psu-id'] = local_var_params['psu_id']  # noqa: E501
        if 'psu_corporate_id' in local_var_params:
            header_params['psu-corporate-id'] = local_var_params['psu_corporate_id']  # noqa: E501
        if 'psu_ip_address' in local_var_params:
            header_params['psu-ip-address'] = local_var_params['psu_ip_address']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_auth_request' in local_var_params:
            body_params = local_var_params['account_auth_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/embedded-account-auth-requests/{consentId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfAuthorisationEmbeddedRequestResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
