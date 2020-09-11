import unittest
from W5_01_arrange_name import rearrange_name

class TestRearrange(unittest.TestCase):

    def test_basic(self):
        #Arrange
        username = "Lovecale, Ada"
        expectedName = "Ada Lovecale"
        #Act
        resultName = rearrange_name(username)
        #Assert
        self.assertEqual(resultName, expectedName)

    def test_empty(self):
        username = ""
        expectedName = ""
        resultName = rearrange_name(username)

        self.assertEqual(resultName, expectedName)

    def test_double_name(self):
        username = "Hopper, Grace M."
        expectedName = "Grace M. Hopper"
        resultName = rearrange_name(username)

        self.assertEqual(resultName, expectedName)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

#unittest.main()