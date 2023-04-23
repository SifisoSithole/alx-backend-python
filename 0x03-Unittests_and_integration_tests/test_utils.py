#!/usr/bin/env python3


from unittest import TestCase, mock
from typing import Mapping, Sequence, Union
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """
    Test cases for the access_nested_map function.
    """
    @parameterized.expand([
        # Test case 1: Access a value at the root level of the map
        ({"a": 1}, ("a",), 1),

        # Test case 2: Access a nested map at the root level of the map
        ({"a": {"b": 2}}, ("a",), {'b': 2}),

        # Test case 3: Access a value in a nested map
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_output: Union[Mapping, int]
    ):
        """
        Test that the access_nested_map function returns the expected
        output for a given input.

        Parameters
        ----------
        nested_map : Mapping
            A nested map to be accessed.
        path : Sequence
            A sequence of keys representing a path to the value to be accessed.
        expected_output : Union[Mapping, int]
            The expected output from accessing the nested
            map with the given path.
        """
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'c'),
        ({"a": 1}, ("a", "b"), 'd')
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, wrong_output
    ):
        """
        Test that accessing a non-existent key in
        a nested map raises a KeyError.

        Parameters
        ----------
        nested_map : Mapping
            A nested map.
        path : Sequence
            A sequence of keys representing a path to the non-existent value.
        wrong_output : str
            A string representation of the wrong output that
            should be raised by the function.

        Raises
        ------
        AssertionError
            If the function does not raise a KeyError
            with the expected wrong output.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(wrong_output, error.exception)


class TestGetJson(TestCase):
    """
    The TestGetJson class contains unit tests for the get_json() function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Mapping):
        """Test the get_json function by mocking the requests.get method.

        Parameters
        ----------
        url : str
            The URL to send the GET request to.
        payload : Mapping
            The expected JSON payload returned by the request.

        Raises
        ------
        AssertionError
            If the response from get_json() does not
            match the expected payload.
        """
        # Mock the requests.get() method to return the specified payload.
        response = mock.Mock()
        response.json.return_value = payload
        with mock.patch('requests.get', return_value=response):
            # Call the get_json() method with the specified URL.
            real_response = get_json(url)

            # Check that the returned payload matches the expected payload.
            self.assertEqual(real_response, payload)

            # Check that the json() method was called exactly once on
            # the response object.
            response.json.assert_called_once()
