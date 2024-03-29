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


class TransactionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_transactions_using_get(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account transactions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_using_get(account_id, consent, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: __Mandatory__. The account Id of the user's bank account. (required)
        :param str consent: __Mandatory__. The `consent-token` containing the user's authorisation to make the request. (required)
        :param str x_yapily_api_version: __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0`
        :param str psu_id: __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_corporate_id: __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_ip_address: __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param list[str] _with: __Optional__. Can be `categories`, `categories-business` or `merchant`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'merchant' enrichment data is requested, the enrichment response will include merchant data only if it can be evaluated from the transaction.
        :param str _from: __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). 
        :param str before: __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).
        :param int limit: __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000.
        :param str sort: __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending
        :param int offset: __Optional__. The number of transaction records to be skipped. Used primarily with paginated results.
        :param str cursor: __Optional__. This property is not currently in use.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiListResponseOfTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transactions_using_get_with_http_info(account_id, consent, **kwargs)  # noqa: E501

    def get_transactions_using_get_with_http_info(self, account_id, consent, **kwargs):  # noqa: E501
        """Get account transactions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_using_get_with_http_info(account_id, consent, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_id: __Mandatory__. The account Id of the user's bank account. (required)
        :param str consent: __Mandatory__. The `consent-token` containing the user's authorisation to make the request. (required)
        :param str x_yapily_api_version: __Optional__. Determines the API version to use. Valid values are `1.0` or `2.0-ALPHA`. Defaults to `1.0`
        :param str psu_id: __Conditional__. Represents the user's login ID for the `Institution` to a personal account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_corporate_id: __Conditional__. Represents the user's login ID for the `Institution` to a business account. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param str psu_ip_address: __Conditional__. The IP address of the PSU. <br><br>See [PSU identifiers](https://docs.yapily.com/knowledge/psu_identifiers/) to see if this header is required.
        :param list[str] _with: __Optional__. Can be `categories`, `categories-business` or `merchant`. When set, will include enrichment data in the transactions returned. <br><br>Enrichment data is optional, e.g. when 'merchant' enrichment data is requested, the enrichment response will include merchant data only if it can be evaluated from the transaction.
        :param str _from: __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). 
        :param str before: __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).
        :param int limit: __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000.
        :param str sort: __Optional__. Sort transaction records by date ascending with 'date' or descending with '-date'. The default sort order is descending
        :param int offset: __Optional__. The number of transaction records to be skipped. Used primarily with paginated results.
        :param str cursor: __Optional__. This property is not currently in use.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiListResponseOfTransaction, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'consent',
            'x_yapily_api_version',
            'psu_id',
            'psu_corporate_id',
            'psu_ip_address',
            '_with',
            '_from',
            'before',
            'limit',
            'sort',
            'offset',
            'cursor'
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
                    " to method get_transactions_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_id` when calling `get_transactions_using_get`")  # noqa: E501
        # verify the required parameter 'consent' is set
        if self.api_client.client_side_validation and ('consent' not in local_var_params or  # noqa: E501
                                                        local_var_params['consent'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consent` when calling `get_transactions_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['accountId'] = local_var_params['account_id']  # noqa: E501

        query_params = []
        if '_with' in local_var_params and local_var_params['_with'] is not None:  # noqa: E501
            query_params.append(('with', local_var_params['_with']))  # noqa: E501
            collection_formats['with'] = 'multi'  # noqa: E501
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
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501

        header_params = {}
        if 'x_yapily_api_version' in local_var_params:
            header_params['x-yapily-api-version'] = local_var_params['x_yapily_api_version']  # noqa: E501
        if 'consent' in local_var_params:
            header_params['consent'] = local_var_params['consent']  # noqa: E501
        if 'psu_id' in local_var_params:
            header_params['psu-id'] = local_var_params['psu_id']  # noqa: E501
        if 'psu_corporate_id' in local_var_params:
            header_params['psu-corporate-id'] = local_var_params['psu_corporate_id']  # noqa: E501
        if 'psu_ip_address' in local_var_params:
            header_params['psu-ip-address'] = local_var_params['psu_ip_address']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/accounts/{accountId}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
