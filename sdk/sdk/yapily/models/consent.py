# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Consent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'consent_token': 'str',
        'feature_scope': 'list[str]',
        'request_id': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'consent_token': 'consentToken',
        'feature_scope': 'featureScope',
        'request_id': 'requestId',
        'token_type': 'tokenType'
    }

    def __init__(self, consent_token=None, feature_scope=None, request_id=None, token_type=None):  # noqa: E501
        """Consent - a model defined in Swagger"""  # noqa: E501

        self._consent_token = None
        self._feature_scope = None
        self._request_id = None
        self._token_type = None
        self.discriminator = None

        if consent_token is not None:
            self.consent_token = consent_token
        if feature_scope is not None:
            self.feature_scope = feature_scope
        if request_id is not None:
            self.request_id = request_id
        if token_type is not None:
            self.token_type = token_type

    @property
    def consent_token(self):
        """Gets the consent_token of this Consent.  # noqa: E501


        :return: The consent_token of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._consent_token

    @consent_token.setter
    def consent_token(self, consent_token):
        """Sets the consent_token of this Consent.


        :param consent_token: The consent_token of this Consent.  # noqa: E501
        :type: str
        """

        self._consent_token = consent_token

    @property
    def feature_scope(self):
        """Gets the feature_scope of this Consent.  # noqa: E501


        :return: The feature_scope of this Consent.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_scope

    @feature_scope.setter
    def feature_scope(self, feature_scope):
        """Sets the feature_scope of this Consent.


        :param feature_scope: The feature_scope of this Consent.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACCOUNTS", "ACCOUNT", "ACCOUNT_TRANSACTIONS", "IDENTITY", "INITIATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENT_INITIATION_DETAILS", "CREATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENTS_DETAILS", "TRANSFER", "OPEN_DATA_PERSONAL_CURRENT_ACCOUNTS", "OPEN_DATA_ATMS"]  # noqa: E501
        if not set(feature_scope).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `feature_scope` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(feature_scope) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._feature_scope = feature_scope

    @property
    def request_id(self):
        """Gets the request_id of this Consent.  # noqa: E501


        :return: The request_id of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Consent.


        :param request_id: The request_id of this Consent.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def token_type(self):
        """Gets the token_type of this Consent.  # noqa: E501


        :return: The token_type of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this Consent.


        :param token_type: The token_type of this Consent.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, Consent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
