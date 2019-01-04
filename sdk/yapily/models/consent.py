# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.55
    
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
        'id': 'str',
        'user_uuid': 'str',
        'institution_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'expires_at': 'datetime',
        'time_to_expire_in_millis': 'int',
        'feature_scope': 'list[str]',
        'consent_token': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_uuid': 'userUuid',
        'institution_id': 'institutionId',
        'status': 'status',
        'created_at': 'createdAt',
        'expires_at': 'expiresAt',
        'time_to_expire_in_millis': 'timeToExpireInMillis',
        'feature_scope': 'featureScope',
        'consent_token': 'consentToken'
    }

    def __init__(self, id=None, user_uuid=None, institution_id=None, status=None, created_at=None, expires_at=None, time_to_expire_in_millis=None, feature_scope=None, consent_token=None):  # noqa: E501
        """Consent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user_uuid = None
        self._institution_id = None
        self._status = None
        self._created_at = None
        self._expires_at = None
        self._time_to_expire_in_millis = None
        self._feature_scope = None
        self._consent_token = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if institution_id is not None:
            self.institution_id = institution_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if expires_at is not None:
            self.expires_at = expires_at
        if time_to_expire_in_millis is not None:
            self.time_to_expire_in_millis = time_to_expire_in_millis
        if feature_scope is not None:
            self.feature_scope = feature_scope
        if consent_token is not None:
            self.consent_token = consent_token

    @property
    def id(self):
        """Gets the id of this Consent.  # noqa: E501


        :return: The id of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Consent.


        :param id: The id of this Consent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this Consent.  # noqa: E501


        :return: The user_uuid of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this Consent.


        :param user_uuid: The user_uuid of this Consent.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def institution_id(self):
        """Gets the institution_id of this Consent.  # noqa: E501


        :return: The institution_id of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this Consent.


        :param institution_id: The institution_id of this Consent.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def status(self):
        """Gets the status of this Consent.  # noqa: E501


        :return: The status of this Consent.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Consent.


        :param status: The status of this Consent.  # noqa: E501
        :type: str
        """
        allowed_values = ["AWAITING_AUTHORIZATION", "AUTHORIZED", "REJECTED", "REVOKED", "FAILED", "EXPIRED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Consent.  # noqa: E501


        :return: The created_at of this Consent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Consent.


        :param created_at: The created_at of this Consent.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def expires_at(self):
        """Gets the expires_at of this Consent.  # noqa: E501


        :return: The expires_at of this Consent.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Consent.


        :param expires_at: The expires_at of this Consent.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def time_to_expire_in_millis(self):
        """Gets the time_to_expire_in_millis of this Consent.  # noqa: E501


        :return: The time_to_expire_in_millis of this Consent.  # noqa: E501
        :rtype: int
        """
        return self._time_to_expire_in_millis

    @time_to_expire_in_millis.setter
    def time_to_expire_in_millis(self, time_to_expire_in_millis):
        """Sets the time_to_expire_in_millis of this Consent.


        :param time_to_expire_in_millis: The time_to_expire_in_millis of this Consent.  # noqa: E501
        :type: int
        """

        self._time_to_expire_in_millis = time_to_expire_in_millis

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
        allowed_values = ["INITIATE_ACCOUNT_REQUEST", "ACCOUNT_REQUEST_DETAILS", "ACCOUNTS", "ACCOUNT", "ACCOUNT_TRANSACTIONS", "ACCOUNT_TRANSACTIONS_WITH_MERCHANT", "IDENTITY", "INITIATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENT_INITIATION_DETAILS", "CREATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENTS_DETAILS", "TRANSFER", "OPEN_DATA_PERSONAL_CURRENT_ACCOUNTS", "OPEN_DATA_ATMS"]  # noqa: E501
        if not set(feature_scope).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `feature_scope` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(feature_scope) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._feature_scope = feature_scope

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
