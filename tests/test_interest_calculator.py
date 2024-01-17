# IMPORTS:
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/gic_calculator')) # set path
from interest_calculator import interest_calc # import interest_caalc function
import math 
import pytest

# TESTING INPUTS:

# Test if the inputs are numeric
def test_assert_numeric_input():
    """Tests that the user inputs are numeric"""
    with pytest.raises(TypeError, match='term_length and principal must be entered as numeric values. gic_rate must be numeric or None type.'):
        interest_calc([2, 4], 90)
    with pytest.raises(TypeError, match='term_length and principal must be entered as numeric values. gic_rate must be numeric or None type.'):
        interest_calc(4000, [2, 4])
    with pytest.raises(TypeError, match='term_length and principal must be entered as numeric values. gic_rate must be numeric or None type.'):
        interest_calc(4000, 180, [2, 4])

# Test if the term_length input is in the allowable range
def test_assert_term_length_range():
    with pytest.raises(ValueError, match='term_length must be provided as one of the following values 90, 180, 270, 1, 1.5, 2, 3, 5.'):
        interest_calc(4000, 524)
    with pytest.raises(ValueError, match='term_length must be provided as one of the following values 90, 180, 270, 1, 1.5, 2, 3, 5.'):
        interest_calc(4000, 524, 4.5)

# Test if the principal input is non-negative
def test_assert_principal_non_negative():
    with pytest.raises(ValueError, match='principal must be entered as a postive numeric value.'):
        interest_calc(-4000, 90)
    with pytest.raises(ValueError, match='principal must be entered as a postive numeric value.'):
        interest_calc(-4000, 90, 4.5)

# Test if the user-specified GIC rate is reasonable
def test_assert_gic_rate_is_realistic():
    with pytest.raises(ValueError, match='gic_rate must be entered as a realistic value between 0 and 7'):
        interest_calc(4000, 90, 8)
    with pytest.raises(ValueError, match='gic_rate must be entered as a realistic value between 0 and 7'):
        interest_calc(4000, 90, -2)
        
# TESTING OUTPUTS:

# For calculations performed with default GIC rates (gic_rate=None)
# Obtain interest_return outputs and store as a dict for each term_length with a principal value of 5000:
principal = 5000
interest_return_dict = {}

for term_length in [90, 180, 270, 1, 1.5, 2, 3, 5]:
    gic_rate, interest_return = interest_calc(principal, term_length, gic_rate=None)
    interest_return_dict[term_length] = interest_return

# Test that the calculated interest returns are equivalent to the expected values.
def test_interest_return_default_input():
    """Test that the calculated interest return matches the actual interest return."""
    expected = {90: 5000 * (1 + 1.4/100) ** (90 / 365) - 5000,
                180: 5000 * (1 + 3.9/100) ** (180 / 365) - 5000,
                270: 5000 * (1 + 5.1/100) ** (270 / 365) - 5000,
                1: 5000 * (1 + 4.9/100) ** (1) - 5000,
                1.5: 5000 * (1 + 4.8/100) ** (1.5) - 5000,
                2: 5000 * (1 + 4.1/100) ** (2) - 5000,
                3: 5000 * (1 + 4.0/100) ** (3) - 5000,
                5: 5000 * (1 + 3.8/100) ** (5) - 5000}
    actual = {90: interest_return_dict[90],
              180: interest_return_dict[180],
              270: interest_return_dict[270],
              1: interest_return_dict[1],
              1.5: interest_return_dict[1.5],
              2: interest_return_dict[2],
              3: interest_return_dict[3],
              5: interest_return_dict[5]}
    
    tolerance = 0.5 # specify acceptable tolerance for deviation between expected and actual. 

    # Test that expected and actual values match within the tolerance
    for key in expected.keys():
        assert abs(expected[key] - actual[key]) <= tolerance, f"Values for key {key} are not equal within the specified tolerance."

# For calculations performed with user-specified GIC rates.
principal = 5000
gic_rate = 5.0
term_length = 1

# Evaluate the expected and actual interest_return values 
def test_interest_return_user_input():
    """Test that the calculated interest return matches the actual interest return."""
    expected = 5000 * (1 + 5.0/100) ** (1) - 5000
    rate, actual = interest_calc(principal, term_length, gic_rate)
    tolerance = 0.5 # specify acceptable tolerance for deviation between expected and actual. 

    # Test that the actual interest returns are equivalent to the expected values within the specified tolerance.
    assert abs(expected - actual) <= tolerance, f"Values for interest_return are not equal within the specified tolerance."