# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.222
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


class StatementsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_statement_file_using_get(self, consent, account_id, statement_id, **kwargs):  # noqa: E501
        """Get account statement file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statement_file_using_get(consent, account_id, statement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param str statement_id: statementId (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_statement_file_using_get_with_http_info(consent, account_id, statement_id, **kwargs)  # noqa: E501

    def get_statement_file_using_get_with_http_info(self, consent, account_id, statement_id, **kwargs):  # noqa: E501
        """Get account statement file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statement_file_using_get_with_http_info(consent, account_id, statement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param str statement_id: statementId (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'consent',
            'account_id',
            'statement_id'
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
                    " to method get_statement_file_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consent' is set
        if self.api_client.client_side_validation and ('consent' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent` when calling `get_statement_file_using_get`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `get_statement_file_using_get`")  # noqa: E501
        # verify the required parameter 'statement_id' is set
        if self.api_client.client_side_validation and ('statement_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['statement_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `statement_id` when calling `get_statement_file_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['accountId'] = local_var_params['account_id']  # noqa: E501
        if 'statement_id' in local_var_params:
            path_params['statementId'] = local_var_params['statement_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consent' in local_var_params:
            header_params['consent'] = local_var_params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/statements/{statementId}/file', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statement_using_get(self, consent, account_id, statement_id, **kwargs):  # noqa: E501
        """Get account statement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statement_using_get(consent, account_id, statement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param str statement_id: statementId (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfAccountStatement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_statement_using_get_with_http_info(consent, account_id, statement_id, **kwargs)  # noqa: E501

    def get_statement_using_get_with_http_info(self, consent, account_id, statement_id, **kwargs):  # noqa: E501
        """Get account statement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statement_using_get_with_http_info(consent, account_id, statement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param str statement_id: statementId (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfAccountStatement, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'consent',
            'account_id',
            'statement_id'
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
                    " to method get_statement_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consent' is set
        if self.api_client.client_side_validation and ('consent' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent` when calling `get_statement_using_get`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `get_statement_using_get`")  # noqa: E501
        # verify the required parameter 'statement_id' is set
        if self.api_client.client_side_validation and ('statement_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['statement_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `statement_id` when calling `get_statement_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['accountId'] = local_var_params['account_id']  # noqa: E501
        if 'statement_id' in local_var_params:
            path_params['statementId'] = local_var_params['statement_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consent' in local_var_params:
            header_params['consent'] = local_var_params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/statements/{statementId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfAccountStatement',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statements_using_get(self, consent, account_id, **kwargs):  # noqa: E501
        """Get account statements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statements_using_get(consent, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param str _from: from
        :param str before: before
        :param int limit: limit
        :param str sort: sort
        :param int offset: offset
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiListResponseOfAccountStatement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_statements_using_get_with_http_info(consent, account_id, **kwargs)  # noqa: E501

    def get_statements_using_get_with_http_info(self, consent, account_id, **kwargs):  # noqa: E501
        """Get account statements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statements_using_get_with_http_info(consent, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str consent: Consent Token (required)
        :param str account_id: accountId (required)
        :param str _from: from
        :param str before: before
        :param int limit: limit
        :param str sort: sort
        :param int offset: offset
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiListResponseOfAccountStatement, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'consent',
            'account_id',
            '_from',
            'before',
            'limit',
            'sort',
            'offset'
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
                    " to method get_statements_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consent' is set
        if self.api_client.client_side_validation and ('consent' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent` when calling `get_statements_using_get`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `get_statements_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['accountId'] = local_var_params['account_id']  # noqa: E501

        query_params = []
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}
        if 'consent' in local_var_params:
            header_params['consent'] = local_var_params['consent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/statements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfAccountStatement',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
