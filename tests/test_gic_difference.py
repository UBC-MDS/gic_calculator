from gic_calculator import gic_difference
import pytest


# Test for equal investment periods and interest rates
def test_equal_periods_and_rates():
    assert calculate_gic_difference(5, 5, 1000, 2.5, 2.5) == 0

# Test for different investment periods with the same interest rate
def test_different_periods_same_rate():
    assert round(calculate_gic_difference(5, 10, 1000, 3.0), 2) == 159.27

# Test for different periods and different interest rates
def test_different_periods_different_rates():
    assert round(calculate_gic_difference(3, 6, 1000, 2.5, 3.5), 2) == 158.76

# Test for scenarios where no interest rates are provided
# This assumes that your function has default interest rates
def test_no_interest_rates():
    expected_value = ...  # Calculate or define the expected value based on default rates
    assert round(calculate_gic_difference(4, 8, 1000), 2) == expected_value

# Test for a scenario where the principal amount is zero
def test_zero_principal():
    assert calculate_gic_difference(5, 10, 0, 2.5, 3.0) == 0

# Test for a scenario where the principal amount is negative
def test_negative_principal():
    with pytest.raises(ValueError):
        calculate_gic_difference(5, 10, -1000, 2.5, 3.0)
