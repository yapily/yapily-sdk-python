# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.157.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Location(object):
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
        'location_category': 'list[str]',
        'other_location_category': 'list[LocationOtherLocationCategory]',
        'postal_address': 'PostalAddress1',
        'site': 'Site',
        'map_service_links': 'ATMMapServiceLinks'
    }

    attribute_map = {
        'location_category': 'LocationCategory',
        'other_location_category': 'OtherLocationCategory',
        'postal_address': 'PostalAddress',
        'site': 'Site',
        'map_service_links': 'mapServiceLinks'
    }

    def __init__(self, location_category=None, other_location_category=None, postal_address=None, site=None, map_service_links=None, local_vars_configuration=None):  # noqa: E501
        """Location - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location_category = None
        self._other_location_category = None
        self._postal_address = None
        self._site = None
        self._map_service_links = None
        self.discriminator = None

        if location_category is not None:
            self.location_category = location_category
        if other_location_category is not None:
            self.other_location_category = other_location_category
        if postal_address is not None:
            self.postal_address = postal_address
        if site is not None:
            self.site = site
        if map_service_links is not None:
            self.map_service_links = map_service_links

    @property
    def location_category(self):
        """Gets the location_category of this Location.  # noqa: E501


        :return: The location_category of this Location.  # noqa: E501
        :rtype: list[str]
        """
        return self._location_category

    @location_category.setter
    def location_category(self, location_category):
        """Sets the location_category of this Location.


        :param location_category: The location_category of this Location.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["BranchExternal", "BranchInternal", "BranchLobby", "Other", "RetailerOutlet", "RemoteUnit"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(location_category).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `location_category` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(location_category) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._location_category = location_category

    @property
    def other_location_category(self):
        """Gets the other_location_category of this Location.  # noqa: E501


        :return: The other_location_category of this Location.  # noqa: E501
        :rtype: list[LocationOtherLocationCategory]
        """
        return self._other_location_category

    @other_location_category.setter
    def other_location_category(self, other_location_category):
        """Sets the other_location_category of this Location.


        :param other_location_category: The other_location_category of this Location.  # noqa: E501
        :type: list[LocationOtherLocationCategory]
        """

        self._other_location_category = other_location_category

    @property
    def postal_address(self):
        """Gets the postal_address of this Location.  # noqa: E501


        :return: The postal_address of this Location.  # noqa: E501
        :rtype: PostalAddress1
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this Location.


        :param postal_address: The postal_address of this Location.  # noqa: E501
        :type: PostalAddress1
        """

        self._postal_address = postal_address

    @property
    def site(self):
        """Gets the site of this Location.  # noqa: E501


        :return: The site of this Location.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this Location.


        :param site: The site of this Location.  # noqa: E501
        :type: Site
        """

        self._site = site

    @property
    def map_service_links(self):
        """Gets the map_service_links of this Location.  # noqa: E501


        :return: The map_service_links of this Location.  # noqa: E501
        :rtype: ATMMapServiceLinks
        """
        return self._map_service_links

    @map_service_links.setter
    def map_service_links(self, map_service_links):
        """Sets the map_service_links of this Location.


        :param map_service_links: The map_service_links of this Location.  # noqa: E501
        :type: ATMMapServiceLinks
        """

        self._map_service_links = map_service_links

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
        if not isinstance(other, Location):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Location):
            return True

        return self.to_dict() != other.to_dict()
