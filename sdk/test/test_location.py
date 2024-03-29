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
from yapily.models.location import Location  # noqa: E501
from yapily.rest import ApiException

class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Location
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.location.Location()  # noqa: E501
        if include_optional :
            return Location(
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
                    here_maps_url = '0', )
            )
        else :
            return Location(
        )

    def testLocation(self):
        """Test Location"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
