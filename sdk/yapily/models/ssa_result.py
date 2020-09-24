# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.245
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class SSAResult(object):
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
        'application_id': 'str',
        'institution_id': 'str',
        'ssa_jwt': 'str'
    }

    attribute_map = {
        'application_id': 'applicationId',
        'institution_id': 'institutionId',
        'ssa_jwt': 'ssaJwt'
    }

    def __init__(self, application_id=None, institution_id=None, ssa_jwt=None, local_vars_configuration=None):  # noqa: E501
        """SSAResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_id = None
        self._institution_id = None
        self._ssa_jwt = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if institution_id is not None:
            self.institution_id = institution_id
        if ssa_jwt is not None:
            self.ssa_jwt = ssa_jwt

    @property
    def application_id(self):
        """Gets the application_id of this SSAResult.  # noqa: E501


        :return: The application_id of this SSAResult.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this SSAResult.


        :param application_id: The application_id of this SSAResult.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def institution_id(self):
        """Gets the institution_id of this SSAResult.  # noqa: E501


        :return: The institution_id of this SSAResult.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this SSAResult.


        :param institution_id: The institution_id of this SSAResult.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def ssa_jwt(self):
        """Gets the ssa_jwt of this SSAResult.  # noqa: E501


        :return: The ssa_jwt of this SSAResult.  # noqa: E501
        :rtype: str
        """
        return self._ssa_jwt

    @ssa_jwt.setter
    def ssa_jwt(self, ssa_jwt):
        """Sets the ssa_jwt of this SSAResult.


        :param ssa_jwt: The ssa_jwt of this SSAResult.  # noqa: E501
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
        if not isinstance(other, SSAResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SSAResult):
            return True

        return self.to_dict() != other.to_dict()
