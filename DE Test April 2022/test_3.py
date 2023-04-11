import pytest
import re

from conftest import test_data, test_error_data
# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    if not re.match(r"^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$", time_str):
        raise ValueError('Incorrect time format.')
    
    list_of_nums = list(map(int, time_str.split(":")))
    return sum(list_of_nums)


@pytest.mark.parametrize("time,sum", test_data)
def test_function(time, sum):
    assert sum_current_time(time) == sum


@pytest.mark.parametrize("time", test_error_data)
def test_invalid_time_format(time):
    with pytest.raises(ValueError):
        sum_current_time(time)
