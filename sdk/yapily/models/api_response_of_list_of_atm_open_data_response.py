# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.157.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class ApiResponseOfListOfATMOpenDataResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'meta': 'ResponseMeta',
        'data': 'list[ATMOpenDataResponse]',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'meta': 'meta',
        'data': 'data',
        'links': 'links'
    }

    def __init__(self, meta=None, data=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ApiResponseOfListOfATMOpenDataResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._meta = None
        self._data = None
        self._links = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if data is not None:
            self.data = data
        if links is not None:
            self.links = links

    @property
    def meta(self):
        """Gets the meta of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501


        :return: The meta of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501
        :rtype: ResponseMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ApiResponseOfListOfATMOpenDataResponse.


        :param meta: The meta of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501
        :type: ResponseMeta
        """

        self._meta = meta

    @property
    def data(self):
        """Gets the data of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501


        :return: The data of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501
        :rtype: list[ATMOpenDataResponse]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiResponseOfListOfATMOpenDataResponse.


        :param data: The data of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501
        :type: list[ATMOpenDataResponse]
        """

        self._data = data

    @property
    def links(self):
        """Gets the links of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501


        :return: The links of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApiResponseOfListOfATMOpenDataResponse.


        :param links: The links of this ApiResponseOfListOfATMOpenDataResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponseOfListOfATMOpenDataResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiResponseOfListOfATMOpenDataResponse):
            return True

        return self.to_dict() != other.to_dict()
