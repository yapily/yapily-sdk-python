# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.297
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class RegistrationRequestAuto(object):
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
        'software_id': 'str',
        'signing_certificate_id': 'str',
        'transport_certificate_id': 'str',
        'ssa_jwt': 'str'
    }

    attribute_map = {
        'software_id': 'softwareId',
        'signing_certificate_id': 'signingCertificateId',
        'transport_certificate_id': 'transportCertificateId',
        'ssa_jwt': 'ssaJwt'
    }

    def __init__(self, software_id=None, signing_certificate_id=None, transport_certificate_id=None, ssa_jwt=None, local_vars_configuration=None):  # noqa: E501
        """RegistrationRequestAuto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._software_id = None
        self._signing_certificate_id = None
        self._transport_certificate_id = None
        self._ssa_jwt = None
        self.discriminator = None

        if software_id is not None:
            self.software_id = software_id
        if signing_certificate_id is not None:
            self.signing_certificate_id = signing_certificate_id
        if transport_certificate_id is not None:
            self.transport_certificate_id = transport_certificate_id
        if ssa_jwt is not None:
            self.ssa_jwt = ssa_jwt

    @property
    def software_id(self):
        """Gets the software_id of this RegistrationRequestAuto.  # noqa: E501


        :return: The software_id of this RegistrationRequestAuto.  # noqa: E501
        :rtype: str
        """
        return self._software_id

    @software_id.setter
    def software_id(self, software_id):
        """Sets the software_id of this RegistrationRequestAuto.


        :param software_id: The software_id of this RegistrationRequestAuto.  # noqa: E501
        :type: str
        """

        self._software_id = software_id

    @property
    def signing_certificate_id(self):
        """Gets the signing_certificate_id of this RegistrationRequestAuto.  # noqa: E501


        :return: The signing_certificate_id of this RegistrationRequestAuto.  # noqa: E501
        :rtype: str
        """
        return self._signing_certificate_id

    @signing_certificate_id.setter
    def signing_certificate_id(self, signing_certificate_id):
        """Sets the signing_certificate_id of this RegistrationRequestAuto.


        :param signing_certificate_id: The signing_certificate_id of this RegistrationRequestAuto.  # noqa: E501
        :type: str
        """

        self._signing_certificate_id = signing_certificate_id

    @property
    def transport_certificate_id(self):
        """Gets the transport_certificate_id of this RegistrationRequestAuto.  # noqa: E501


        :return: The transport_certificate_id of this RegistrationRequestAuto.  # noqa: E501
        :rtype: str
        """
        return self._transport_certificate_id

    @transport_certificate_id.setter
    def transport_certificate_id(self, transport_certificate_id):
        """Sets the transport_certificate_id of this RegistrationRequestAuto.


        :param transport_certificate_id: The transport_certificate_id of this RegistrationRequestAuto.  # noqa: E501
        :type: str
        """

        self._transport_certificate_id = transport_certificate_id

    @property
    def ssa_jwt(self):
        """Gets the ssa_jwt of this RegistrationRequestAuto.  # noqa: E501


        :return: The ssa_jwt of this RegistrationRequestAuto.  # noqa: E501
        :rtype: str
        """
        return self._ssa_jwt

    @ssa_jwt.setter
    def ssa_jwt(self, ssa_jwt):
        """Sets the ssa_jwt of this RegistrationRequestAuto.


        :param ssa_jwt: The ssa_jwt of this RegistrationRequestAuto.  # noqa: E501
        :type: str
        """

        self._ssa_jwt = ssa_jwt

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
        if not isinstance(other, RegistrationRequestAuto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistrationRequestAuto):
            return True

        return self.to_dict() != other.to_dict()
