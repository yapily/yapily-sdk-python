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


class CreditInterestTierBandSet(object):
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
        'calculation_method': 'str',
        'credit_interest_eligibility': 'list[CreditInterestCreditInterestEligibility]',
        'destination': 'str',
        'notes': 'list[str]',
        'tier_band': 'list[CreditInterestTierBand]',
        'tier_band_method': 'str'
    }

    attribute_map = {
        'calculation_method': 'CalculationMethod',
        'credit_interest_eligibility': 'CreditInterestEligibility',
        'destination': 'Destination',
        'notes': 'Notes',
        'tier_band': 'TierBand',
        'tier_band_method': 'TierBandMethod'
    }

    def __init__(self, calculation_method=None, credit_interest_eligibility=None, destination=None, notes=None, tier_band=None, tier_band_method=None, local_vars_configuration=None):  # noqa: E501
        """CreditInterestTierBandSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._calculation_method = None
        self._credit_interest_eligibility = None
        self._destination = None
        self._notes = None
        self._tier_band = None
        self._tier_band_method = None
        self.discriminator = None

        if calculation_method is not None:
            self.calculation_method = calculation_method
        if credit_interest_eligibility is not None:
            self.credit_interest_eligibility = credit_interest_eligibility
        if destination is not None:
            self.destination = destination
        if notes is not None:
            self.notes = notes
        if tier_band is not None:
            self.tier_band = tier_band
        if tier_band_method is not None:
            self.tier_band_method = tier_band_method

    @property
    def calculation_method(self):
        """Gets the calculation_method of this CreditInterestTierBandSet.  # noqa: E501


        :return: The calculation_method of this CreditInterestTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this CreditInterestTierBandSet.


        :param calculation_method: The calculation_method of this CreditInterestTierBandSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Compound", "SimpleInterest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and calculation_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `calculation_method` ({0}), must be one of {1}"  # noqa: E501
                .format(calculation_method, allowed_values)
            )

        self._calculation_method = calculation_method

    @property
    def credit_interest_eligibility(self):
        """Gets the credit_interest_eligibility of this CreditInterestTierBandSet.  # noqa: E501


        :return: The credit_interest_eligibility of this CreditInterestTierBandSet.  # noqa: E501
        :rtype: list[CreditInterestCreditInterestEligibility]
        """
        return self._credit_interest_eligibility

    @credit_interest_eligibility.setter
    def credit_interest_eligibility(self, credit_interest_eligibility):
        """Sets the credit_interest_eligibility of this CreditInterestTierBandSet.


        :param credit_interest_eligibility: The credit_interest_eligibility of this CreditInterestTierBandSet.  # noqa: E501
        :type: list[CreditInterestCreditInterestEligibility]
        """

        self._credit_interest_eligibility = credit_interest_eligibility

    @property
    def destination(self):
        """Gets the destination of this CreditInterestTierBandSet.  # noqa: E501


        :return: The destination of this CreditInterestTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this CreditInterestTierBandSet.


        :param destination: The destination of this CreditInterestTierBandSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["PayAway", "SelfCredit"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and destination not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `destination` ({0}), must be one of {1}"  # noqa: E501
                .format(destination, allowed_values)
            )

        self._destination = destination

    @property
    def notes(self):
        """Gets the notes of this CreditInterestTierBandSet.  # noqa: E501


        :return: The notes of this CreditInterestTierBandSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreditInterestTierBandSet.


        :param notes: The notes of this CreditInterestTierBandSet.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def tier_band(self):
        """Gets the tier_band of this CreditInterestTierBandSet.  # noqa: E501


        :return: The tier_band of this CreditInterestTierBandSet.  # noqa: E501
        :rtype: list[CreditInterestTierBand]
        """
        return self._tier_band

    @tier_band.setter
    def tier_band(self, tier_band):
        """Sets the tier_band of this CreditInterestTierBandSet.


        :param tier_band: The tier_band of this CreditInterestTierBandSet.  # noqa: E501
        :type: list[CreditInterestTierBand]
        """

        self._tier_band = tier_band

    @property
    def tier_band_method(self):
        """Gets the tier_band_method of this CreditInterestTierBandSet.  # noqa: E501


        :return: The tier_band_method of this CreditInterestTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._tier_band_method

    @tier_band_method.setter
    def tier_band_method(self, tier_band_method):
        """Sets the tier_band_method of this CreditInterestTierBandSet.


        :param tier_band_method: The tier_band_method of this CreditInterestTierBandSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tiered", "Whole"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tier_band_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tier_band_method` ({0}), must be one of {1}"  # noqa: E501
                .format(tier_band_method, allowed_values)
            )

        self._tier_band_method = tier_band_method

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
        if not isinstance(other, CreditInterestTierBandSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditInterestTierBandSet):
            return True

        return self.to_dict() != other.to_dict()
