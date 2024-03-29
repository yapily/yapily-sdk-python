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


class Enrichment(object):
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
        'categorisation': 'Categorisation',
        'transaction_hash': 'TransactionHash',
        'cleansed_description': 'str',
        'merchant': 'EnrichmentMerchant',
        'location': 'str',
        'payment_processor': 'str',
        'corrected_date': 'datetime'
    }

    attribute_map = {
        'categorisation': 'categorisation',
        'transaction_hash': 'transactionHash',
        'cleansed_description': 'cleansedDescription',
        'merchant': 'merchant',
        'location': 'location',
        'payment_processor': 'paymentProcessor',
        'corrected_date': 'correctedDate'
    }

    def __init__(self, categorisation=None, transaction_hash=None, cleansed_description=None, merchant=None, location=None, payment_processor=None, corrected_date=None, local_vars_configuration=None):  # noqa: E501
        """Enrichment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._categorisation = None
        self._transaction_hash = None
        self._cleansed_description = None
        self._merchant = None
        self._location = None
        self._payment_processor = None
        self._corrected_date = None
        self.discriminator = None

        if categorisation is not None:
            self.categorisation = categorisation
        if transaction_hash is not None:
            self.transaction_hash = transaction_hash
        if cleansed_description is not None:
            self.cleansed_description = cleansed_description
        if merchant is not None:
            self.merchant = merchant
        if location is not None:
            self.location = location
        if payment_processor is not None:
            self.payment_processor = payment_processor
        if corrected_date is not None:
            self.corrected_date = corrected_date

    @property
    def categorisation(self):
        """Gets the categorisation of this Enrichment.  # noqa: E501


        :return: The categorisation of this Enrichment.  # noqa: E501
        :rtype: Categorisation
        """
        return self._categorisation

    @categorisation.setter
    def categorisation(self, categorisation):
        """Sets the categorisation of this Enrichment.


        :param categorisation: The categorisation of this Enrichment.  # noqa: E501
        :type: Categorisation
        """

        self._categorisation = categorisation

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this Enrichment.  # noqa: E501


        :return: The transaction_hash of this Enrichment.  # noqa: E501
        :rtype: TransactionHash
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this Enrichment.


        :param transaction_hash: The transaction_hash of this Enrichment.  # noqa: E501
        :type: TransactionHash
        """

        self._transaction_hash = transaction_hash

    @property
    def cleansed_description(self):
        """Gets the cleansed_description of this Enrichment.  # noqa: E501

        CleansedDescription  # noqa: E501

        :return: The cleansed_description of this Enrichment.  # noqa: E501
        :rtype: str
        """
        return self._cleansed_description

    @cleansed_description.setter
    def cleansed_description(self, cleansed_description):
        """Sets the cleansed_description of this Enrichment.

        CleansedDescription  # noqa: E501

        :param cleansed_description: The cleansed_description of this Enrichment.  # noqa: E501
        :type: str
        """

        self._cleansed_description = cleansed_description

    @property
    def merchant(self):
        """Gets the merchant of this Enrichment.  # noqa: E501


        :return: The merchant of this Enrichment.  # noqa: E501
        :rtype: EnrichmentMerchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this Enrichment.


        :param merchant: The merchant of this Enrichment.  # noqa: E501
        :type: EnrichmentMerchant
        """

        self._merchant = merchant

    @property
    def location(self):
        """Gets the location of this Enrichment.  # noqa: E501

        Location  # noqa: E501

        :return: The location of this Enrichment.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Enrichment.

        Location  # noqa: E501

        :param location: The location of this Enrichment.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def payment_processor(self):
        """Gets the payment_processor of this Enrichment.  # noqa: E501

        PaymentProcessor  # noqa: E501

        :return: The payment_processor of this Enrichment.  # noqa: E501
        :rtype: str
        """
        return self._payment_processor

    @payment_processor.setter
    def payment_processor(self, payment_processor):
        """Sets the payment_processor of this Enrichment.

        PaymentProcessor  # noqa: E501

        :param payment_processor: The payment_processor of this Enrichment.  # noqa: E501
        :type: str
        """

        self._payment_processor = payment_processor

    @property
    def corrected_date(self):
        """Gets the corrected_date of this Enrichment.  # noqa: E501

        CorrectedDate  # noqa: E501

        :return: The corrected_date of this Enrichment.  # noqa: E501
        :rtype: datetime
        """
        return self._corrected_date

    @corrected_date.setter
    def corrected_date(self, corrected_date):
        """Sets the corrected_date of this Enrichment.

        CorrectedDate  # noqa: E501

        :param corrected_date: The corrected_date of this Enrichment.  # noqa: E501
        :type: datetime
        """

        self._corrected_date = corrected_date

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
        if not isinstance(other, Enrichment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Enrichment):
            return True

        return self.to_dict() != other.to_dict()
