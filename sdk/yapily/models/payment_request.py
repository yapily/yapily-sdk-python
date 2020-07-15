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


class PaymentRequest(object):
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
        'payment_idempotency_id': 'str',
        'payer': 'Payer',
        'amount': 'Amount',
        'reference': 'str',
        'context_type': 'str',
        'type': 'str',
        'payment_date_time': 'datetime',
        'payee': 'Payee',
        'periodic_payment': 'PeriodicPaymentRequest',
        'international_payment': 'InternationalPaymentRequest'
    }

    attribute_map = {
        'payment_idempotency_id': 'paymentIdempotencyId',
        'payer': 'payer',
        'amount': 'amount',
        'reference': 'reference',
        'context_type': 'contextType',
        'type': 'type',
        'payment_date_time': 'paymentDateTime',
        'payee': 'payee',
        'periodic_payment': 'periodicPayment',
        'international_payment': 'internationalPayment'
    }

    def __init__(self, payment_idempotency_id=None, payer=None, amount=None, reference=None, context_type=None, type=None, payment_date_time=None, payee=None, periodic_payment=None, international_payment=None, local_vars_configuration=None):  # noqa: E501
        """PaymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment_idempotency_id = None
        self._payer = None
        self._amount = None
        self._reference = None
        self._context_type = None
        self._type = None
        self._payment_date_time = None
        self._payee = None
        self._periodic_payment = None
        self._international_payment = None
        self.discriminator = None

        if payment_idempotency_id is not None:
            self.payment_idempotency_id = payment_idempotency_id
        if payer is not None:
            self.payer = payer
        if amount is not None:
            self.amount = amount
        if reference is not None:
            self.reference = reference
        if context_type is not None:
            self.context_type = context_type
        self.type = type
        if payment_date_time is not None:
            self.payment_date_time = payment_date_time
        self.payee = payee
        if periodic_payment is not None:
            self.periodic_payment = periodic_payment
        if international_payment is not None:
            self.international_payment = international_payment

    @property
    def payment_idempotency_id(self):
        """Gets the payment_idempotency_id of this PaymentRequest.  # noqa: E501


        :return: The payment_idempotency_id of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_idempotency_id

    @payment_idempotency_id.setter
    def payment_idempotency_id(self, payment_idempotency_id):
        """Sets the payment_idempotency_id of this PaymentRequest.


        :param payment_idempotency_id: The payment_idempotency_id of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self._payment_idempotency_id = payment_idempotency_id

    @property
    def payer(self):
        """Gets the payer of this PaymentRequest.  # noqa: E501


        :return: The payer of this PaymentRequest.  # noqa: E501
        :rtype: Payer
        """
        return self._payer

    @payer.setter
    def payer(self, payer):
        """Sets the payer of this PaymentRequest.


        :param payer: The payer of this PaymentRequest.  # noqa: E501
        :type: Payer
        """

        self._payer = payer

    @property
    def amount(self):
        """Gets the amount of this PaymentRequest.  # noqa: E501


        :return: The amount of this PaymentRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRequest.


        :param amount: The amount of this PaymentRequest.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def reference(self):
        """Gets the reference of this PaymentRequest.  # noqa: E501


        :return: The reference of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentRequest.


        :param reference: The reference of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def context_type(self):
        """Gets the context_type of this PaymentRequest.  # noqa: E501


        :return: The context_type of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """Sets the context_type of this PaymentRequest.


        :param context_type: The context_type of this PaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BILL", "GOODS", "SERVICES", "OTHER", "PERSON_TO_PERSON"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and context_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `context_type` ({0}), must be one of {1}"  # noqa: E501
                .format(context_type, allowed_values)
            )

        self._context_type = context_type

    @property
    def type(self):
        """Gets the type of this PaymentRequest.  # noqa: E501


        :return: The type of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentRequest.


        :param type: The type of this PaymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["DOMESTIC_PAYMENT", "DOMESTIC_INSTANT_PAYMENT", "DOMESTIC_VARIABLE_RECURRING_PAYMENT", "DOMESTIC_SCHEDULED_PAYMENT", "DOMESTIC_PERIODIC_PAYMENT", "INTERNATIONAL_PAYMENT", "INTERNATIONAL_SCHEDULED_PAYMENT", "INTERNATIONAL_PERIODIC_PAYMENT", "BULK_PAYMENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def payment_date_time(self):
        """Gets the payment_date_time of this PaymentRequest.  # noqa: E501


        :return: The payment_date_time of this PaymentRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date_time

    @payment_date_time.setter
    def payment_date_time(self, payment_date_time):
        """Sets the payment_date_time of this PaymentRequest.


        :param payment_date_time: The payment_date_time of this PaymentRequest.  # noqa: E501
        :type: datetime
        """

        self._payment_date_time = payment_date_time

    @property
    def payee(self):
        """Gets the payee of this PaymentRequest.  # noqa: E501


        :return: The payee of this PaymentRequest.  # noqa: E501
        :rtype: Payee
        """
        return self._payee

    @payee.setter
    def payee(self, payee):
        """Sets the payee of this PaymentRequest.


        :param payee: The payee of this PaymentRequest.  # noqa: E501
        :type: Payee
        """
        if self.local_vars_configuration.client_side_validation and payee is None:  # noqa: E501
            raise ValueError("Invalid value for `payee`, must not be `None`")  # noqa: E501

        self._payee = payee

    @property
    def periodic_payment(self):
        """Gets the periodic_payment of this PaymentRequest.  # noqa: E501


        :return: The periodic_payment of this PaymentRequest.  # noqa: E501
        :rtype: PeriodicPaymentRequest
        """
        return self._periodic_payment

    @periodic_payment.setter
    def periodic_payment(self, periodic_payment):
        """Sets the periodic_payment of this PaymentRequest.


        :param periodic_payment: The periodic_payment of this PaymentRequest.  # noqa: E501
        :type: PeriodicPaymentRequest
        """

        self._periodic_payment = periodic_payment

    @property
    def international_payment(self):
        """Gets the international_payment of this PaymentRequest.  # noqa: E501


        :return: The international_payment of this PaymentRequest.  # noqa: E501
        :rtype: InternationalPaymentRequest
        """
        return self._international_payment

    @international_payment.setter
    def international_payment(self, international_payment):
        """Sets the international_payment of this PaymentRequest.


        :param international_payment: The international_payment of this PaymentRequest.  # noqa: E501
        :type: InternationalPaymentRequest
        """

        self._international_payment = international_payment

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
        if not isinstance(other, PaymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentRequest):
            return True

        return self.to_dict() != other.to_dict()
