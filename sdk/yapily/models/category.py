# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.124.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Category(object):
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
        'id': 'str',
        'label': 'str',
        'country': 'str',
        'subcategories': 'list[Subcategory]'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'country': 'country',
        'subcategories': 'subcategories'
    }

    def __init__(self, id=None, label=None, country=None, subcategories=None, local_vars_configuration=None):  # noqa: E501
        """Category - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._label = None
        self._country = None
        self._subcategories = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if country is not None:
            self.country = country
        if subcategories is not None:
            self.subcategories = subcategories

    @property
    def id(self):
        """Gets the id of this Category.  # noqa: E501

        Category ID  # noqa: E501

        :return: The id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Category.

        Category ID  # noqa: E501

        :param id: The id of this Category.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Category.  # noqa: E501

        Category label  # noqa: E501

        :return: The label of this Category.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Category.

        Category label  # noqa: E501

        :param label: The label of this Category.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def country(self):
        """Gets the country of this Category.  # noqa: E501

        Category country  # noqa: E501

        :return: The country of this Category.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Category.

        Category country  # noqa: E501

        :param country: The country of this Category.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def subcategories(self):
        """Gets the subcategories of this Category.  # noqa: E501


        :return: The subcategories of this Category.  # noqa: E501
        :rtype: list[Subcategory]
        """
        return self._subcategories

    @subcategories.setter
    def subcategories(self, subcategories):
        """Sets the subcategories of this Category.


        :param subcategories: The subcategories of this Category.  # noqa: E501
        :type: list[Subcategory]
        """

        self._subcategories = subcategories

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
        if not isinstance(other, Category):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Category):
            return True

        return self.to_dict() != other.to_dict()
