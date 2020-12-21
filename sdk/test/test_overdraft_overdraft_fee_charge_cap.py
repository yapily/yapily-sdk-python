# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.294
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.overdraft_overdraft_fee_charge_cap import OverdraftOverdraftFeeChargeCap  # noqa: E501
from yapily.rest import ApiException

class TestOverdraftOverdraftFeeChargeCap(unittest.TestCase):
    """OverdraftOverdraftFeeChargeCap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OverdraftOverdraftFeeChargeCap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.overdraft_overdraft_fee_charge_cap.OverdraftOverdraftFeeChargeCap()  # noqa: E501
        if include_optional :
            return OverdraftOverdraftFeeChargeCap(
                capping_period = 'Day', 
                fee_cap_amount = '0', 
                fee_cap_occurrence = 1.337, 
                fee_type = [
                    'ArrangedOverdraft'
                    ], 
                min_max_type = 'Minimum', 
                notes = [
                    '0'
                    ], 
                other_fee_type = [
                    yapily.models.overdraft_other_fee_type.OverdraftOtherFeeType(
                        code = '0', 
                        description = '0', 
                        name = '0', )
                    ], 
                overdraft_control_indicator = True
            )
        else :
            return OverdraftOverdraftFeeChargeCap(
        )

    def testOverdraftOverdraftFeeChargeCap(self):
        """Test OverdraftOverdraftFeeChargeCap"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
