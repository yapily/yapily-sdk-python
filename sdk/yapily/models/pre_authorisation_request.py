# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.289
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class PreAuthorisationRequest(object):
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
        'scope': 'str',
        'user_uuid': 'str',
        'application_user_id': 'str',
        'forward_parameters': 'list[str]',
        'institution_id': 'str',
        'callback': 'str',
        'one_time_token': 'bool'
    }

    attribute_map = {
        'scope': 'scope',
        'user_uuid': 'userUuid',
        'application_user_id': 'applicationUserId',
        'forward_parameters': 'forwardParameters',
        'institution_id': 'institutionId',
        'callback': 'callback',
        'one_time_token': 'oneTimeToken'
    }

    def __init__(self, scope=None, user_uuid=None, application_user_id=None, forward_parameters=None, institution_id=None, callback=None, one_time_token=None, local_vars_configuration=None):  # noqa: E501
        """PreAuthorisationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scope = None
        self._user_uuid = None
        self._application_user_id = None
        self._forward_parameters = None
        self._institution_id = None
        self._callback = None
        self._one_time_token = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if application_user_id is not None:
            self.application_user_id = application_user_id
        if forward_parameters is not None:
            self.forward_parameters = forward_parameters
        self.institution_id = institution_id
        self.callback = callback
        self.one_time_token = one_time_token

    @property
    def scope(self):
        """Gets the scope of this PreAuthorisationRequest.  # noqa: E501


        :return: The scope of this PreAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PreAuthorisationRequest.


        :param scope: The scope of this PreAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def user_uuid(self):
        """Gets the user_uuid of this PreAuthorisationRequest.  # noqa: E501

        Uuid of the application user who will authorise access to their data. Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :return: The user_uuid of this PreAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this PreAuthorisationRequest.

        Uuid of the application user who will authorise access to their data. Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :param user_uuid: The user_uuid of this PreAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def application_user_id(self):
        """Gets the application_user_id of this PreAuthorisationRequest.  # noqa: E501

        Descriptive identifier for the application user.Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :return: The application_user_id of this PreAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_user_id

    @application_user_id.setter
    def application_user_id(self, application_user_id):
        """Sets the application_user_id of this PreAuthorisationRequest.

        Descriptive identifier for the application user.Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :param application_user_id: The application_user_id of this PreAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._application_user_id = application_user_id

    @property
    def forward_parameters(self):
        """Gets the forward_parameters of this PreAuthorisationRequest.  # noqa: E501


        :return: The forward_parameters of this PreAuthorisationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._forward_parameters

    @forward_parameters.setter
    def forward_parameters(self, forward_parameters):
        """Sets the forward_parameters of this PreAuthorisationRequest.


        :param forward_parameters: The forward_parameters of this PreAuthorisationRequest.  # noqa: E501
        :type: list[str]
        """

        self._forward_parameters = forward_parameters

    @property
    def institution_id(self):
        """Gets the institution_id of this PreAuthorisationRequest.  # noqa: E501


        :return: The institution_id of this PreAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this PreAuthorisationRequest.


        :param institution_id: The institution_id of this PreAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and institution_id is None:  # noqa: E501
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def callback(self):
        """Gets the callback of this PreAuthorisationRequest.  # noqa: E501


        :return: The callback of this PreAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this PreAuthorisationRequest.


        :param callback: The callback of this PreAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and callback is None:  # noqa: E501
            raise ValueError("Invalid value for `callback`, must not be `None`")  # noqa: E501

        self._callback = callback

    @property
    def one_time_token(self):
        """Gets the one_time_token of this PreAuthorisationRequest.  # noqa: E501


        :return: The one_time_token of this PreAuthorisationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._one_time_token

    @one_time_token.setter
    def one_time_token(self, one_time_token):
        """Sets the one_time_token of this PreAuthorisationRequest.


        :param one_time_token: The one_time_token of this PreAuthorisationRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and one_time_token is None:  # noqa: E501
            raise ValueError("Invalid value for `one_time_token`, must not be `None`")  # noqa: E501

        self._one_time_token = one_time_token

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
        if not isinstance(other, PreAuthorisationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PreAuthorisationRequest):
            return True

        return self.to_dict() != other.to_dict()
