# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.209
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class MultiAuthorisation(object):
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
        'status': 'str',
        'number_of_authorisation_required': 'int',
        'number_of_authorisation_received': 'int',
        'last_updated_date_time': 'datetime',
        'expiration_date_time': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'number_of_authorisation_required': 'numberOfAuthorisationRequired',
        'number_of_authorisation_received': 'numberOfAuthorisationReceived',
        'last_updated_date_time': 'lastUpdatedDateTime',
        'expiration_date_time': 'expirationDateTime'
    }

    def __init__(self, status=None, number_of_authorisation_required=None, number_of_authorisation_received=None, last_updated_date_time=None, expiration_date_time=None, local_vars_configuration=None):  # noqa: E501
        """MultiAuthorisation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._number_of_authorisation_required = None
        self._number_of_authorisation_received = None
        self._last_updated_date_time = None
        self._expiration_date_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if number_of_authorisation_required is not None:
            self.number_of_authorisation_required = number_of_authorisation_required
        if number_of_authorisation_received is not None:
            self.number_of_authorisation_received = number_of_authorisation_received
        if last_updated_date_time is not None:
            self.last_updated_date_time = last_updated_date_time
        if expiration_date_time is not None:
            self.expiration_date_time = expiration_date_time

    @property
    def status(self):
        """Gets the status of this MultiAuthorisation.  # noqa: E501


        :return: The status of this MultiAuthorisation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MultiAuthorisation.


        :param status: The status of this MultiAuthorisation.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def number_of_authorisation_required(self):
        """Gets the number_of_authorisation_required of this MultiAuthorisation.  # noqa: E501


        :return: The number_of_authorisation_required of this MultiAuthorisation.  # noqa: E501
        :rtype: int
        """
        return self._number_of_authorisation_required

    @number_of_authorisation_required.setter
    def number_of_authorisation_required(self, number_of_authorisation_required):
        """Sets the number_of_authorisation_required of this MultiAuthorisation.


        :param number_of_authorisation_required: The number_of_authorisation_required of this MultiAuthorisation.  # noqa: E501
        :type: int
        """

        self._number_of_authorisation_required = number_of_authorisation_required

    @property
    def number_of_authorisation_received(self):
        """Gets the number_of_authorisation_received of this MultiAuthorisation.  # noqa: E501


        :return: The number_of_authorisation_received of this MultiAuthorisation.  # noqa: E501
        :rtype: int
        """
        return self._number_of_authorisation_received

    @number_of_authorisation_received.setter
    def number_of_authorisation_received(self, number_of_authorisation_received):
        """Sets the number_of_authorisation_received of this MultiAuthorisation.


        :param number_of_authorisation_received: The number_of_authorisation_received of this MultiAuthorisation.  # noqa: E501
        :type: int
        """

        self._number_of_authorisation_received = number_of_authorisation_received

    @property
    def last_updated_date_time(self):
        """Gets the last_updated_date_time of this MultiAuthorisation.  # noqa: E501


        :return: The last_updated_date_time of this MultiAuthorisation.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date_time

    @last_updated_date_time.setter
    def last_updated_date_time(self, last_updated_date_time):
        """Sets the last_updated_date_time of this MultiAuthorisation.


        :param last_updated_date_time: The last_updated_date_time of this MultiAuthorisation.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date_time = last_updated_date_time

    @property
    def expiration_date_time(self):
        """Gets the expiration_date_time of this MultiAuthorisation.  # noqa: E501


        :return: The expiration_date_time of this MultiAuthorisation.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_time

    @expiration_date_time.setter
    def expiration_date_time(self, expiration_date_time):
        """Sets the expiration_date_time of this MultiAuthorisation.


        :param expiration_date_time: The expiration_date_time of this MultiAuthorisation.  # noqa: E501
        :type: datetime
        """

        self._expiration_date_time = expiration_date_time

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
        if not isinstance(other, MultiAuthorisation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiAuthorisation):
            return True

        return self.to_dict() != other.to_dict()
