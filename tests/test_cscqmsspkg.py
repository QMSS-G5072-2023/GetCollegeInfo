import pytest
from cscqmsspkg import cscqmsspkg
from get_college_info import get_college_info


def test_get_college_info():
    college_name_input = "Michigan State University"
    api_key = "api_key"
    result = get_college_info(college_name_input, api_key)
    assert result is not None
    assert result["Name"] == college_name_input

    invalid_college_name = "Invalid College Name"
    result_invalid = get_college_info(invalid_college_name, dummy_api_key)
    assert result_invalid is None

def test_invalid_api_key():
    college_name_input = "Rutgers University-New Brunswick"
    invalid_api_key = "invalid_api_key"

    result = get_college_info(college_name_input, invalid_api_key)
    assert result is None

def test_multiple_college_matches():
    college_name_input = "State"
    api_key = "api_key"

    result = get_college_info(college_name_input, api_key)
    assert result is None
