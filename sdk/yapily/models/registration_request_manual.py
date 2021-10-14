# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.127.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class RegistrationRequestManual(object):
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
        'client_id': 'str',
        'client_secret': 'str',
        'tpp_id': 'str',
        'software_id': 'str',
        'client_name': 'str',
        'signing_key_id': 'str',
        'signing_certificate_id': 'str',
        'transport_key_id': 'str',
        'transport_certificate_id': 'str',
        'client_uri': 'str',
        'terms_of_service_uri': 'str',
        'ssa_jwt': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'tpp_id': 'tppId',
        'software_id': 'softwareId',
        'client_name': 'clientName',
        'signing_key_id': 'signingKeyId',
        'signing_certificate_id': 'signingCertificateId',
        'transport_key_id': 'transportKeyId',
        'transport_certificate_id': 'transportCertificateId',
        'client_uri': 'clientUri',
        'terms_of_service_uri': 'termsOfServiceUri',
        'ssa_jwt': 'ssaJwt'
    }

    def __init__(self, client_id=None, client_secret=None, tpp_id=None, software_id=None, client_name=None, signing_key_id=None, signing_certificate_id=None, transport_key_id=None, transport_certificate_id=None, client_uri=None, terms_of_service_uri=None, ssa_jwt=None, local_vars_configuration=None):  # noqa: E501
        """RegistrationRequestManual - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._client_secret = None
        self._tpp_id = None
        self._software_id = None
        self._client_name = None
        self._signing_key_id = None
        self._signing_certificate_id = None
        self._transport_key_id = None
        self._transport_certificate_id = None
        self._client_uri = None
        self._terms_of_service_uri = None
        self._ssa_jwt = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if tpp_id is not None:
            self.tpp_id = tpp_id
        if software_id is not None:
            self.software_id = software_id
        if client_name is not None:
            self.client_name = client_name
        if signing_key_id is not None:
            self.signing_key_id = signing_key_id
        if signing_certificate_id is not None:
            self.signing_certificate_id = signing_certificate_id
        if transport_key_id is not None:
            self.transport_key_id = transport_key_id
        if transport_certificate_id is not None:
            self.transport_certificate_id = transport_certificate_id
        if client_uri is not None:
            self.client_uri = client_uri
        if terms_of_service_uri is not None:
            self.terms_of_service_uri = terms_of_service_uri
        if ssa_jwt is not None:
            self.ssa_jwt = ssa_jwt

    @property
    def client_id(self):
        """Gets the client_id of this RegistrationRequestManual.  # noqa: E501


        :return: The client_id of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RegistrationRequestManual.


        :param client_id: The client_id of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this RegistrationRequestManual.  # noqa: E501


        :return: The client_secret of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this RegistrationRequestManual.


        :param client_secret: The client_secret of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def tpp_id(self):
        """Gets the tpp_id of this RegistrationRequestManual.  # noqa: E501


        :return: The tpp_id of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._tpp_id

    @tpp_id.setter
    def tpp_id(self, tpp_id):
        """Sets the tpp_id of this RegistrationRequestManual.


        :param tpp_id: The tpp_id of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._tpp_id = tpp_id

    @property
    def software_id(self):
        """Gets the software_id of this RegistrationRequestManual.  # noqa: E501


        :return: The software_id of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._software_id

    @software_id.setter
    def software_id(self, software_id):
        """Sets the software_id of this RegistrationRequestManual.


        :param software_id: The software_id of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._software_id = software_id

    @property
    def client_name(self):
        """Gets the client_name of this RegistrationRequestManual.  # noqa: E501


        :return: The client_name of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this RegistrationRequestManual.


        :param client_name: The client_name of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def signing_key_id(self):
        """Gets the signing_key_id of this RegistrationRequestManual.  # noqa: E501


        :return: The signing_key_id of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._signing_key_id

    @signing_key_id.setter
    def signing_key_id(self, signing_key_id):
        """Sets the signing_key_id of this RegistrationRequestManual.


        :param signing_key_id: The signing_key_id of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._signing_key_id = signing_key_id

    @property
    def signing_certificate_id(self):
        """Gets the signing_certificate_id of this RegistrationRequestManual.  # noqa: E501


        :return: The signing_certificate_id of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._signing_certificate_id

    @signing_certificate_id.setter
    def signing_certificate_id(self, signing_certificate_id):
        """Sets the signing_certificate_id of this RegistrationRequestManual.


        :param signing_certificate_id: The signing_certificate_id of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._signing_certificate_id = signing_certificate_id

    @property
    def transport_key_id(self):
        """Gets the transport_key_id of this RegistrationRequestManual.  # noqa: E501


        :return: The transport_key_id of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._transport_key_id

    @transport_key_id.setter
    def transport_key_id(self, transport_key_id):
        """Sets the transport_key_id of this RegistrationRequestManual.


        :param transport_key_id: The transport_key_id of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._transport_key_id = transport_key_id

    @property
    def transport_certificate_id(self):
        """Gets the transport_certificate_id of this RegistrationRequestManual.  # noqa: E501


        :return: The transport_certificate_id of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._transport_certificate_id

    @transport_certificate_id.setter
    def transport_certificate_id(self, transport_certificate_id):
        """Sets the transport_certificate_id of this RegistrationRequestManual.


        :param transport_certificate_id: The transport_certificate_id of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._transport_certificate_id = transport_certificate_id

    @property
    def client_uri(self):
        """Gets the client_uri of this RegistrationRequestManual.  # noqa: E501


        :return: The client_uri of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._client_uri

    @client_uri.setter
    def client_uri(self, client_uri):
        """Sets the client_uri of this RegistrationRequestManual.


        :param client_uri: The client_uri of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._client_uri = client_uri

    @property
    def terms_of_service_uri(self):
        """Gets the terms_of_service_uri of this RegistrationRequestManual.  # noqa: E501


        :return: The terms_of_service_uri of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._terms_of_service_uri

    @terms_of_service_uri.setter
    def terms_of_service_uri(self, terms_of_service_uri):
        """Sets the terms_of_service_uri of this RegistrationRequestManual.


        :param terms_of_service_uri: The terms_of_service_uri of this RegistrationRequestManual.  # noqa: E501
        :type: str
        """

        self._terms_of_service_uri = terms_of_service_uri

    @property
    def ssa_jwt(self):
        """Gets the ssa_jwt of this RegistrationRequestManual.  # noqa: E501


        :return: The ssa_jwt of this RegistrationRequestManual.  # noqa: E501
        :rtype: str
        """
        return self._ssa_jwt

    @ssa_jwt.setter
    def ssa_jwt(self, ssa_jwt):
        """Sets the ssa_jwt of this RegistrationRequestManual.


        :param ssa_jwt: The ssa_jwt of this RegistrationRequestManual.  # noqa: E501
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
        if not isinstance(other, RegistrationRequestManual):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistrationRequestManual):
            return True

        return self.to_dict() != other.to_dict()
