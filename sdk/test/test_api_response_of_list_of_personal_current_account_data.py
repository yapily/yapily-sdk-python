# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.157.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_response_of_list_of_personal_current_account_data import ApiResponseOfListOfPersonalCurrentAccountData  # noqa: E501
from yapily.rest import ApiException

class TestApiResponseOfListOfPersonalCurrentAccountData(unittest.TestCase):
    """ApiResponseOfListOfPersonalCurrentAccountData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseOfListOfPersonalCurrentAccountData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_response_of_list_of_personal_current_account_data.ApiResponseOfListOfPersonalCurrentAccountData()  # noqa: E501
        if include_optional :
            return ApiResponseOfListOfPersonalCurrentAccountData(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '0', ), 
                data = [
                    yapily.models.personal_current_account_data.PersonalCurrentAccountData(
                        brand = [
                            yapily.models.personal_current_account_brand.PersonalCurrentAccountBrand(
                                brand_name = '0', 
                                pca = [
                                    yapily.models.personal_current_account_pca.PersonalCurrentAccountPCA(
                                        identification = '0', 
                                        name = '0', 
                                        pca_marketing_state = [
                                            yapily.models.personal_current_account_pca_marketing_state.PersonalCurrentAccountPCAMarketingState(
                                                core_product = yapily.models.core_product.CoreProduct(
                                                    monthly_maximum_charge = '0', 
                                                    product_description = '0', 
                                                    product_url = '0', 
                                                    sales_access_channels = [
                                                        'Branch'
                                                        ], 
                                                    servicing_access_channels = [
                                                        'ATM'
                                                        ], 
                                                    tcs_and_cs_url = '0', ), 
                                                credit_interest = yapily.models.credit_interest.CreditInterest(
                                                    tier_band_set = [
                                                        yapily.models.credit_interest_tier_band_set.CreditInterestTierBandSet(
                                                            calculation_method = 'Compound', 
                                                            credit_interest_eligibility = [
                                                                yapily.models.credit_interest_credit_interest_eligibility.CreditInterestCreditInterestEligibility(
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
                                                            destination = 'PayAway', 
                                                            notes = [
                                                                '0'
                                                                ], 
                                                            tier_band = [
                                                                yapily.models.credit_interest_tier_band.CreditInterestTierBand(
                                                                    aer = '0', 
                                                                    application_frequency = 'PerAcademicTerm', 
                                                                    bank_interest_rate = '0', 
                                                                    bank_interest_rate_type = 'LinkedBaseRate', 
                                                                    calculation_frequency = 'PerAcademicTerm', 
                                                                    deposit_interest_applied_coverage = 'Tiered', 
                                                                    fixed_variable_interest_rate_type = 'Fixed', 
                                                                    identification = '0', 
                                                                    other_application_frequency = yapily.models.other_application_frequency.OtherApplicationFrequency(
                                                                        code = '0', 
                                                                        description = '0', 
                                                                        name = '0', ), 
                                                                    other_bank_interest_type = yapily.models.other_bank_interest_type.OtherBankInterestType(
                                                                        code = '0', 
                                                                        description = '0', 
                                                                        name = '0', ), 
                                                                    other_calculation_frequency = yapily.models.other_calculation_frequency.OtherCalculationFrequency(
                                                                        code = '0', 
                                                                        description = '0', 
                                                                        name = '0', ), 
                                                                    tier_value_maximum = '0', 
                                                                    tier_value_minimum = '0', )
                                                                ], 
                                                            tier_band_method = 'Tiered', )
                                                        ], ), 
                                                eligibility = yapily.models.eligibility.Eligibility(
                                                    age_eligibility = yapily.models.age_eligibility.AgeEligibility(
                                                        maximum_age = 1.337, 
                                                        minimum_age = 1.337, ), 
                                                    credit_check = yapily.models.credit_check.CreditCheck(
                                                        scoring_type = 'Hard', ), 
                                                    id_verification_check = yapily.models.id_verification_check.IDVerificationCheck(
                                                        url = '0', ), 
                                                    other_eligibility = [
                                                        yapily.models.eligibility_other_eligibility.EligibilityOtherEligibility(
                                                            amount = '0', 
                                                            description = '0', 
                                                            indicator = True, 
                                                            name = '0', 
                                                            period = 'Day', 
                                                            textual = '0', 
                                                            type = 'DirectDebits', )
                                                        ], 
                                                    residency_eligibility = yapily.models.residency_eligibility.ResidencyEligibility(
                                                        other_residency_type = yapily.models.other_residency_type.OtherResidencyType(
                                                            code = '0', 
                                                            description = '0', 
                                                            name = '0', ), 
                                                        residency_included = [
                                                            '0'
                                                            ], 
                                                        residency_type = 'Householder', ), ), 
                                                first_marketed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                identification = '0', 
                                                last_marketed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                marketing_state = '0', 
                                                notes = [
                                                    '0'
                                                    ], 
                                                overdraft = yapily.models.overdraft.Overdraft(
                                                    overdraft_tier_band_set = [
                                                        yapily.models.overdraft_overdraft_tier_band_set.OverdraftOverdraftTierBandSet(
                                                            authorised_indicator = True, 
                                                            buffer_amount = '0', 
                                                            identification = '0', 
                                                            minimum_arranged_overdraft_amount = '0', 
                                                            overdraft_fees_charges = [
                                                                yapily.models.overdraft_overdraft_fees_charges1.OverdraftOverdraftFeesCharges1(
                                                                    overdraft_fee_charge_cap = [
                                                                        yapily.models.overdraft_overdraft_fee_charge_cap.OverdraftOverdraftFeeChargeCap(
                                                                            capping_period = 'Day', 
                                                                            fee_cap_amount = '0', 
                                                                            fee_cap_occurrence = 1.337, 
                                                                            fee_type = [
                                                                                'ArrangedOverdraft'
                                                                                ], 
                                                                            min_max_type = 'Minimum', 
                                                                            other_fee_type = [
                                                                                yapily.models.overdraft_other_fee_type.OverdraftOtherFeeType(
                                                                                    code = '0', 
                                                                                    description = '0', 
                                                                                    name = '0', )
                                                                                ], 
                                                                            overdraft_control_indicator = True, )
                                                                        ], 
                                                                    overdraft_fee_charge_detail = [
                                                                        yapily.models.overdraft_overdraft_fee_charge_detail.OverdraftOverdraftFeeChargeDetail(
                                                                            application_frequency = 'AccountClosing', 
                                                                            calculation_frequency = 'AccountClosing', 
                                                                            fee_amount = '0', 
                                                                            fee_rate = '0', 
                                                                            fee_rate_type = 'LinkedBaseRate', 
                                                                            incremental_borrowing_amount = '0', 
                                                                            other_fee_rate_type = yapily.models.other_fee_rate_type.OtherFeeRateType(
                                                                                code = '0', 
                                                                                description = '0', 
                                                                                name = '0', ), 
                                                                            overdraft_control_indicator = True, )
                                                                        ], )
                                                                ], 
                                                            overdraft_tier_band = [
                                                                yapily.models.overdraft_overdraft_tier_band.OverdraftOverdraftTierBand(
                                                                    bank_guaranteed_indicator = True, 
                                                                    ear = '0', 
                                                                    identification = '0', 
                                                                    overdraft_interest_charging_coverage = 'Tiered', 
                                                                    tier_value_max = '0', 
                                                                    tier_value_min = '0', )
                                                                ], 
                                                            overdraft_type = 'Committed', 
                                                            tier_band_method = 'Tiered', )
                                                        ], 
                                                    tcs_and_cs_url = '0', ), 
                                                predecessor_id = '0', 
                                                state_tenure_length = 1.337, 
                                                state_tenure_period = '0', )
                                            ], 
                                        segment = [
                                            '0'
                                            ], )
                                    ], )
                            ], )
                    ], 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiResponseOfListOfPersonalCurrentAccountData(
        )

    def testApiResponseOfListOfPersonalCurrentAccountData(self):
        """Test ApiResponseOfListOfPersonalCurrentAccountData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
