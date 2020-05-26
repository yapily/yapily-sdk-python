# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.189
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.eligibility import Eligibility  # noqa: E501
from yapily.rest import ApiException

class TestEligibility(unittest.TestCase):
    """Eligibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Eligibility
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.eligibility.Eligibility()  # noqa: E501
        if include_optional :
            return Eligibility(
                age_eligibility = yapily.models.age_eligibility.AgeEligibility(
                    maximum_age = 1.337, 
                    minimum_age = 1.337, 
                    notes = [
                        '0'
                        ], ), 
                credit_check = yapily.models.credit_check.CreditCheck(
                    notes = [
                        '0'
                        ], 
                    scoring_type = 'Hard', ), 
                id_verification_check = yapily.models.id_verification_check.IDVerificationCheck(
                    notes = [
                        '0'
                        ], 
                    url = '0', ), 
                other_eligibility = [
                    yapily.models.eligibility_other_eligibility.EligibilityOtherEligibility(
                        amount = '0', 
                        description = '0', 
                        indicator = True, 
                        name = '0', 
                        notes = [
                            '0'
                            ], 
                        other_type = yapily.models.other_type.OtherType(
                            code = '0', 
                            description = '0', 
                            name = '0', ), 
                        period = 'Day', 
                        textual = '0', 
                        type = 'DirectDebits', )
                    ], 
                residency_eligibility = yapily.models.residency_eligibility.ResidencyEligibility(
                    notes = [
                        '0'
                        ], 
                    other_residency_type = yapily.models.other_residency_type.OtherResidencyType(
                        code = '0', 
                        description = '0', 
                        name = '0', ), 
                    residency_included = [
                        '0'
                        ], 
                    residency_type = 'Householder', )
            )
        else :
            return Eligibility(
        )

    def testEligibility(self):
        """Test Eligibility"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
