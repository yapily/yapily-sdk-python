# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.154.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class AccountInfo(object):
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
        'account_id': 'str',
        'account_identification': 'AccountIdentification'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_identification': 'accountIdentification'
    }

    def __init__(self, account_id=None, account_identification=None, local_vars_configuration=None):  # noqa: E501
        """AccountInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._account_identification = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_identification is not None:
            self.account_identification = account_identification

    @property
    def account_id(self):
        """Gets the account_id of this AccountInfo.  # noqa: E501


        :return: The account_id of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountInfo.


        :param account_id: The account_id of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_identification(self):
        """Gets the account_identification of this AccountInfo.  # noqa: E501


        :return: The account_identification of this AccountInfo.  # noqa: E501
        :rtype: AccountIdentification
        """
        return self._account_identification

    @account_identification.setter
    def account_identification(self, account_identification):
        """Sets the account_identification of this AccountInfo.


        :param account_identification: The account_identification of this AccountInfo.  # noqa: E501
        :type: AccountIdentification
        """

        self._account_identification = account_identification

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
        if not isinstance(other, AccountInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountInfo):
            return True

        return self.to_dict() != other.to_dict()
