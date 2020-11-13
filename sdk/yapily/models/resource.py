# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.273
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Resource(object):
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
        'description': 'str',
        'file': 'file',
        'filename': 'str',
        'input_stream': 'object',
        'open': 'bool',
        'readable': 'bool',
        'uri': 'str',
        'url': 'URL'
    }

    attribute_map = {
        'description': 'description',
        'file': 'file',
        'filename': 'filename',
        'input_stream': 'inputStream',
        'open': 'open',
        'readable': 'readable',
        'uri': 'uri',
        'url': 'url'
    }

    def __init__(self, description=None, file=None, filename=None, input_stream=None, open=None, readable=None, uri=None, url=None, local_vars_configuration=None):  # noqa: E501
        """Resource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._file = None
        self._filename = None
        self._input_stream = None
        self._open = None
        self._readable = None
        self._uri = None
        self._url = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if file is not None:
            self.file = file
        if filename is not None:
            self.filename = filename
        if input_stream is not None:
            self.input_stream = input_stream
        if open is not None:
            self.open = open
        if readable is not None:
            self.readable = readable
        if uri is not None:
            self.uri = uri
        if url is not None:
            self.url = url

    @property
    def description(self):
        """Gets the description of this Resource.  # noqa: E501


        :return: The description of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Resource.


        :param description: The description of this Resource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file(self):
        """Gets the file of this Resource.  # noqa: E501


        :return: The file of this Resource.  # noqa: E501
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Resource.


        :param file: The file of this Resource.  # noqa: E501
        :type: file
        """

        self._file = file

    @property
    def filename(self):
        """Gets the filename of this Resource.  # noqa: E501


        :return: The filename of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Resource.


        :param filename: The filename of this Resource.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def input_stream(self):
        """Gets the input_stream of this Resource.  # noqa: E501


        :return: The input_stream of this Resource.  # noqa: E501
        :rtype: object
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this Resource.


        :param input_stream: The input_stream of this Resource.  # noqa: E501
        :type: object
        """

        self._input_stream = input_stream

    @property
    def open(self):
        """Gets the open of this Resource.  # noqa: E501


        :return: The open of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this Resource.


        :param open: The open of this Resource.  # noqa: E501
        :type: bool
        """

        self._open = open

    @property
    def readable(self):
        """Gets the readable of this Resource.  # noqa: E501


        :return: The readable of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._readable

    @readable.setter
    def readable(self, readable):
        """Sets the readable of this Resource.


        :param readable: The readable of this Resource.  # noqa: E501
        :type: bool
        """

        self._readable = readable

    @property
    def uri(self):
        """Gets the uri of this Resource.  # noqa: E501


        :return: The uri of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Resource.


        :param uri: The uri of this Resource.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def url(self):
        """Gets the url of this Resource.  # noqa: E501


        :return: The url of this Resource.  # noqa: E501
        :rtype: URL
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Resource.


        :param url: The url of this Resource.  # noqa: E501
        :type: URL
        """

        self._url = url

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
        if not isinstance(other, Resource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Resource):
            return True

        return self.to_dict() != other.to_dict()
