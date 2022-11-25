"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.15.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from yapily.api_client import ApiClient, Endpoint as _Endpoint
from yapily.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from yapily.model.api_error_response import ApiErrorResponse
from yapily.model.api_list_response_of_consent import ApiListResponseOfConsent
from yapily.model.api_response_error import ApiResponseError
from yapily.model.api_response_of_consent import ApiResponseOfConsent
from yapily.model.api_response_of_consent_delete_response import ApiResponseOfConsentDeleteResponse
from yapily.model.consent import Consent
from yapily.model.consent_auth_code_request import ConsentAuthCodeRequest
from yapily.model.extend_consent_request import ExtendConsentRequest
from yapily.model.one_time_token_request import OneTimeTokenRequest


class ConsentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_consent_with_code_endpoint = _Endpoint(
            settings={
                'response_type': (Consent,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/consent-auth-code',
                'operation_id': 'create_consent_with_code',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'consent_auth_code_request',
                ],
                'required': [
                    'consent_auth_code_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'consent_auth_code_request':
                        (ConsentAuthCodeRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'consent_auth_code_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_endpoint = _Endpoint(
            settings={
                'response_type': (ApiResponseOfConsentDeleteResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/consents/{consentId}',
                'operation_id': 'delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'consent_id',
                    'force_delete',
                ],
                'required': [
                    'consent_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'consent_id':
                        (str,),
                    'force_delete':
                        (bool,),
                },
                'attribute_map': {
                    'consent_id': 'consentId',
                    'force_delete': 'forceDelete',
                },
                'location_map': {
                    'consent_id': 'path',
                    'force_delete': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.extend_consent_endpoint = _Endpoint(
            settings={
                'response_type': (ApiResponseOfConsent,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/consents/{consentId}/extend',
                'operation_id': 'extend_consent',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'consent_id',
                    'extend_consent_request',
                ],
                'required': [
                    'consent_id',
                    'extend_consent_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'consent_id':
                        (str,),
                    'extend_consent_request':
                        (ExtendConsentRequest,),
                },
                'attribute_map': {
                    'consent_id': 'consentId',
                },
                'location_map': {
                    'consent_id': 'path',
                    'extend_consent_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [
                    'application/json;charset=UTF-8'
                ]
            },
            api_client=api_client
        )
        self.get_consent_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (ApiResponseOfConsent,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/consents/{consentId}',
                'operation_id': 'get_consent_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'consent_id',
                ],
                'required': [
                    'consent_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'consent_id':
                        (str,),
                },
                'attribute_map': {
                    'consent_id': 'consentId',
                },
                'location_map': {
                    'consent_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_consent_by_single_access_consent_endpoint = _Endpoint(
            settings={
                'response_type': (Consent,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/consent-one-time-token',
                'operation_id': 'get_consent_by_single_access_consent',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'one_time_token_request',
                ],
                'required': [
                    'one_time_token_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'one_time_token_request':
                        (OneTimeTokenRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'one_time_token_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_consents_endpoint = _Endpoint(
            settings={
                'response_type': (ApiListResponseOfConsent,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/consents',
                'operation_id': 'get_consents',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_application_user_id',
                    'filter_user_uuid',
                    'filter_institution',
                    'filter_status',
                    'from',
                    'before',
                    'limit',
                    'offset',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'filter_application_user_id',
                    'filter_user_uuid',
                    'filter_institution',
                    'filter_status',
                ]
            },
            root_map={
                'validations': {
                    ('filter_application_user_id',): {

                    },
                    ('filter_user_uuid',): {

                    },
                    ('filter_institution',): {

                    },
                    ('filter_status',): {

                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'filter_application_user_id':
                        ([str],),
                    'filter_user_uuid':
                        ([str],),
                    'filter_institution':
                        ([str],),
                    'filter_status':
                        ([str],),
                    'from':
                        (str,),
                    'before':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'filter_application_user_id': 'filter[applicationUserId]',
                    'filter_user_uuid': 'filter[userUuid]',
                    'filter_institution': 'filter[institution]',
                    'filter_status': 'filter[status]',
                    'from': 'from',
                    'before': 'before',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'filter_application_user_id': 'query',
                    'filter_user_uuid': 'query',
                    'filter_institution': 'query',
                    'filter_status': 'query',
                    'from': 'query',
                    'before': 'query',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                    'filter_application_user_id': 'multi',
                    'filter_user_uuid': 'multi',
                    'filter_institution': 'multi',
                    'filter_status': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_consent_with_code(
        self,
        consent_auth_code_request,
        **kwargs
    ):
        """Exchange OAuth2 Code  # noqa: E501

        Used to obtain a Yapily Consent object containing the `consentToken` once the user has authenticated and you have an OAuth2 authorisation code `auth-code` and state `auth-state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_consent_with_code(consent_auth_code_request, async_req=True)
        >>> result = thread.get()

        Args:
            consent_auth_code_request (ConsentAuthCodeRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Consent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['consent_auth_code_request'] = \
            consent_auth_code_request
        return self.create_consent_with_code_endpoint.call_with_http_info(**kwargs)

    def delete(
        self,
        consent_id,
        **kwargs
    ):
        """Delete Consent  # noqa: E501

        Delete a consent using the consent Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete(consent_id, async_req=True)
        >>> result = thread.get()

        Args:
            consent_id (str): __Mandatory__. The consent Id of the `Consent` to update.

        Keyword Args:
            force_delete (bool): __Optional__. Whether to force the deletion.. [optional] if omitted the server will use the default value of True
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiResponseOfConsentDeleteResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['consent_id'] = \
            consent_id
        return self.delete_endpoint.call_with_http_info(**kwargs)

    def extend_consent(
        self,
        consent_id,
        extend_consent_request,
        **kwargs
    ):
        """Extend Consent  # noqa: E501

        Used to indicate to Yapily that reconfirmation has occurred for a given Consent, and to update lastUpdatedAt and reconfirmBy for that Consent. Returns the Consent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.extend_consent(consent_id, extend_consent_request, async_req=True)
        >>> result = thread.get()

        Args:
            consent_id (str): __Mandatory__. The consent Id of the `Consent` to update.
            extend_consent_request (ExtendConsentRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiResponseOfConsent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['consent_id'] = \
            consent_id
        kwargs['extend_consent_request'] = \
            extend_consent_request
        return self.extend_consent_endpoint.call_with_http_info(**kwargs)

    def get_consent_by_id(
        self,
        consent_id,
        **kwargs
    ):
        """Get Consent  # noqa: E501

        Get consent using the consent Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_consent_by_id(consent_id, async_req=True)
        >>> result = thread.get()

        Args:
            consent_id (str): __Mandatory__. The consent Id of the `Consent` to update.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiResponseOfConsent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['consent_id'] = \
            consent_id
        return self.get_consent_by_id_endpoint.call_with_http_info(**kwargs)

    def get_consent_by_single_access_consent(
        self,
        one_time_token_request,
        **kwargs
    ):
        """Exchange One Time Token  # noqa: E501

        Exchange a One-time-token for the consent token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_consent_by_single_access_consent(one_time_token_request, async_req=True)
        >>> result = thread.get()

        Args:
            one_time_token_request (OneTimeTokenRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Consent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['one_time_token_request'] = \
            one_time_token_request
        return self.get_consent_by_single_access_consent_endpoint.call_with_http_info(**kwargs)

    def get_consents(
        self,
        **kwargs
    ):
        """Get Consents  # noqa: E501

        Used to retrieve all the consents created for each user within an application  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_consents(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_application_user_id ([str]): __Optional__. Filter records based on the list of `applicationUserId` users provided.. [optional]
            filter_user_uuid ([str]): __Optional__. Filter records based on the list of `userUuid` users provided.. [optional]
            filter_institution ([str]): __Optional__. Filter records based on the list of `Institution` provided.. [optional]
            filter_status ([str]): __Optional__. Filter records based on the list of `Consent` [statuses](https://docs.yapily.com/api/reference/#operation/getConsents!c=200&path=data/status&t=response).. [optional]
            from (str): __Optional__. Returned transactions will be on or after this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ). . [optional]
            before (str): __Optional__. Returned transactions will be on or before this date (yyyy-MM-dd'T'HH:mm:ss.SSSZ).. [optional]
            limit (int): __Optional__. The maximum number of transaction records to be returned. Must be between 0 and 1000.. [optional]
            offset (int): __Optional__. The number of transaction records to be skipped. Used primarily with paginated results.. [optional] if omitted the server will use the default value of 0
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ApiListResponseOfConsent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_consents_endpoint.call_with_http_info(**kwargs)

