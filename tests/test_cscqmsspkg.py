import pytest
from cscqmsspkg import cscqmsspkg
from get_college_info import get_college_info


def test_get_college_info():
    college_name_input = "Michigan State University"
    result = get_college_info(college_name_input, api_key)
    assert result is not None
    assert result["Name"] == college_name_input

    # Test case for invalid college name
    invalid_college_name = "Invalid College Name"
    result_invalid = get_college_info(invalid_college_name, dummy_api_key)
    assert result_invalid is None