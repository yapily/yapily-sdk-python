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
from yapily.models.inline_response2001_atm import InlineResponse2001ATM  # noqa: E501
from yapily.rest import ApiException

class TestInlineResponse2001ATM(unittest.TestCase):
    """InlineResponse2001ATM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2001ATM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.inline_response2001_atm.InlineResponse2001ATM()  # noqa: E501
        if include_optional :
            return InlineResponse2001ATM(
                atm_services = [
                    'Balance'
                    ], 
                access24_hours_indicator = True, 
                accessibility = [
                    'AudioCashMachine'
                    ], 
                branch = yapily.models.branch.Branch(
                    identification = '0', ), 
                identification = '0', 
                location = yapily.models.location.Location(
                    location_category = [
                        'BranchExternal'
                        ], 
                    other_location_category = [
                        yapily.models.location_other_location_category.LocationOtherLocationCategory(
                            code = '0', 
                            description = '0', 
                            name = '0', )
                        ], 
                    postal_address = yapily.models.postal_address1.PostalAddress1(
                        address_line = [
                            '0'
                            ], 
                        building_number = '0', 
                        country = '0', 
                        country_sub_division = [
                            '0'
                            ], 
                        geo_location = yapily.models.geo_location1.GeoLocation1(
                            geographic_coordinates = yapily.models.geographic_coordinates1.GeographicCoordinates1(
                                latitude = '0', 
                                longitude = '0', ), ), 
                        post_code = '0', 
                        street_name = '0', 
                        town_name = '0', ), 
                    site = yapily.models.site.Site(
                        identification = '0', 
                        name = '0', ), 
                    map_service_links = yapily.models.atm_map_service_links.ATMMapServiceLinks(
                        bing_maps_url = '0', 
                        google_maps_url = '0', 
                        here_maps_url = '0', ), ), 
                minimum_possible_amount = '0', 
                note = [
                    '0'
                    ], 
                other_atm_services = [
                    yapily.models.inline_response2001_other_atm_services.InlineResponse2001OtherATMServices(
                        code = '0', 
                        description = '0', 
                        name = '0', )
                    ], 
                other_accessibility = [
                    yapily.models.inline_response2001_other_accessibility.InlineResponse2001OtherAccessibility(
                        code = '0', 
                        description = '0', 
                        name = '0', )
                    ], 
                supported_currencies = [
                    '0'
                    ], 
                supported_languages = [
                    '0'
                    ]
            )
        else :
            return InlineResponse2001ATM(
        )

    def testInlineResponse2001ATM(self):
        """Test InlineResponse2001ATM"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
