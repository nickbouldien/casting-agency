import unittest
from ..utils import check_valid_age


class UtilityTestCase(unittest.TestCase):
    """This class tests the utility functions"""

    def setUp(self):
        self.valid_age = 47
        self.valid_age_str = "34"
        self.invalid_age_not_integer = "not an integer"
        self.invalid_age_negative_number = -18
        self.invalid_age_none = None
        self.invalid_age_empty_string = ""

    # check_valid_age tests
    def check_valid_age_success(self):
        """Tests check_valid_age success"""
        self.assertEqual(True, check_valid_age(self.valid_age))
        self.assertEqual(True, check_valid_age(self.valid_age))

    def check_valid_age_failure(self):
        """Tests check_valid_age failure"""
        self.assertEqual(False, check_valid_age(self.invalid_age_not_integer))
        self.assertEqual(False, check_valid_age(self.invalid_age_negative_number))
        self.assertEqual(False, check_valid_age(self.invalid_age_none))
        self.assertEqual(False, check_valid_age(self.invalid_age_empty_string))
