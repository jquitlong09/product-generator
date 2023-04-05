import unittest
from v1.helpers.validator import Validator
from v1.helpers.openapi import OpenAPI

validator = Validator()
openapi = OpenAPI()


class GenericTest(unittest.TestCase):

    def test_validate_required(self):
        # Test case 1
        required = ['name', 'age']
        param = {'name': 'John', 'age': '20'}
        result = validator.validate_required(required, param)
        assert result == True

        # Test case 2
        required = ['name', 'age']
        param = {'name': 'John'}
        result = validator.validate_required(required, param)
        assert result == False


    def test_get_product_names(self):
        # Create a param object
        param = {
            "product_description": "summer dress",
            "vibe_words": "romantic"
        }

        # Call the get_product_names() method
        product_names = openapi.get_product_names(param)

        # Assert that the returned list is not empty
        assert product_names != []

    def test_get_one_add(test):
        # Create mock data
        product = "iPhone 11"
        description = "It has a great camera"
        template = "The {0} is the best phone ever. {1}."
        
        # Assert that return string is not empty or blank
        actual_result = openapi.get_one_add(product, description, template)
        assert len(actual_result) > 0


if __name__ == '__main__':
    unittest.main()