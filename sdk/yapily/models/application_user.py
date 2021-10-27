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


class ApplicationUser(object):
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
        'application_user_id': 'str',
        'application_uuid': 'str',
        'institution_consents': 'list[InstitutionConsent]',
        'reference_id': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'application_user_id': 'applicationUserId',
        'application_uuid': 'applicationUuid',
        'institution_consents': 'institutionConsents',
        'reference_id': 'referenceId',
        'uuid': 'uuid'
    }

    def __init__(self, application_user_id=None, application_uuid=None, institution_consents=None, reference_id=None, uuid=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_user_id = None
        self._application_uuid = None
        self._institution_consents = None
        self._reference_id = None
        self._uuid = None
        self.discriminator = None

        if application_user_id is not None:
            self.application_user_id = application_user_id
        if application_uuid is not None:
            self.application_uuid = application_uuid
        if institution_consents is not None:
            self.institution_consents = institution_consents
        if reference_id is not None:
            self.reference_id = reference_id
        if uuid is not None:
            self.uuid = uuid

    @property
    def application_user_id(self):
        """Gets the application_user_id of this ApplicationUser.  # noqa: E501


        :return: The application_user_id of this ApplicationUser.  # noqa: E501
        :rtype: str
        """
        return self._application_user_id

    @application_user_id.setter
    def application_user_id(self, application_user_id):
        """Sets the application_user_id of this ApplicationUser.


        :param application_user_id: The application_user_id of this ApplicationUser.  # noqa: E501
        :type: str
        """

        self._application_user_id = application_user_id

    @property
    def application_uuid(self):
        """Gets the application_uuid of this ApplicationUser.  # noqa: E501


        :return: The application_uuid of this ApplicationUser.  # noqa: E501
        :rtype: str
        """
        return self._application_uuid

    @application_uuid.setter
    def application_uuid(self, application_uuid):
        """Sets the application_uuid of this ApplicationUser.


        :param application_uuid: The application_uuid of this ApplicationUser.  # noqa: E501
        :type: str
        """

        self._application_uuid = application_uuid

    @property
    def institution_consents(self):
        """Gets the institution_consents of this ApplicationUser.  # noqa: E501


        :return: The institution_consents of this ApplicationUser.  # noqa: E501
        :rtype: list[InstitutionConsent]
        """
        return self._institution_consents

    @institution_consents.setter
    def institution_consents(self, institution_consents):
        """Sets the institution_consents of this ApplicationUser.


        :param institution_consents: The institution_consents of this ApplicationUser.  # noqa: E501
        :type: list[InstitutionConsent]
        """

        self._institution_consents = institution_consents

    @property
    def reference_id(self):
        """Gets the reference_id of this ApplicationUser.  # noqa: E501


        :return: The reference_id of this ApplicationUser.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this ApplicationUser.


        :param reference_id: The reference_id of this ApplicationUser.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def uuid(self):
        """Gets the uuid of this ApplicationUser.  # noqa: E501


        :return: The uuid of this ApplicationUser.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ApplicationUser.


        :param uuid: The uuid of this ApplicationUser.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, ApplicationUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationUser):
            return True

        return self.to_dict() != other.to_dict()
