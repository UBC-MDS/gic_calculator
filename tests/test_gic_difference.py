from gic_calculator.gic_difference import calculate_gic_difference
import pytest


# Test for equal investment periods and interest rates
def test_equal_periods_and_rates():
    # Both periods are 1 year
    assert calculate_gic_difference(1, 1, 1000, 2.5, 2.5) == 0

# Test for different periods and different interest rates
def test_different_periods_different_rates():
    assert round(calculate_gic_difference(1, 2, 1000, 2.5, 3.5), 2) == 46.22

# Test for scenarios where no interest rates are provided
def test_no_interest_rates():
    expected_difference = calculate_gic_difference(1, 2, 1000, 4.9, 4.1)
    assert round(calculate_gic_difference(1, 2, 1000), 2) == round(expected_difference, 2)

# Test for a scenario where the principal amount is zero
def test_zero_principal():
    assert calculate_gic_difference(1, 2, 0, 2.5, 3.0) == 0

# Test for a scenario where the principal amount is negative
def test_negative_principal():
    with pytest.raises(ValueError):
        calculate_gic_difference(1, 2, -1000, 2.5, 3.0)

# Test if the inputs are numeric
def test_assert_numeric_input():
    """Tests that the user inputs are numeric"""
    with pytest.raises(TypeError):
        calculate_gic_difference([1, 3], 90, 1000, 2.5, 3.0)
    with pytest.raises(TypeError):
        calculate_gic_difference(90, [1, 3], 1000, 2.5, 3.0)
    with pytest.raises(TypeError):
        calculate_gic_difference(1, 90, '1000', 2.5, 3.0)
    with pytest.raises(TypeError):
        calculate_gic_difference(1, 90, 1000, '2.5', 3.0)
    with pytest.raises(TypeError):
        calculate_gic_difference(1, 90, 1000, 2.5, '3.0')

# Test if the term_length input is in the allowable range
def test_assert_term_length_range():
    with pytest.raises(ValueError):
        calculate_gic_difference(524, 90, 1000, 2.5, 3.0)
    with pytest.raises(ValueError):
        calculate_gic_difference(90, 524, 1000, 2.5, 3.0)