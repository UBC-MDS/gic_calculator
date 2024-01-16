from src.gic_calculator import gic_plotting
import pytest

principal_valid = 1000.0
gic_rates_valid = [1.0, 2.1]
term_lengths_valid = [90, 1.5]

principal_invalid = ['string', -1000, 0]
gic_rates_invalid = ['string', 1.0, [], [1.0, 2.1, 3.2]]
term_lengths_invalid = ['string', 1.5, [], [90, 1, 270]]

# Test gic_plotting function can output Altair Chart with valid inputs
def test_gic_plotting_valid_inputs():
    assert isinstance(gic_plotting(principal_valid, None, term_lengths_valid), alt.Chart), "`gic_plotting` should return an Altair Chart object"
    assert isinstance(gic_plotting(principal_valid, gic_rates_valid, term_lengths_valid), alt.Chart), "`gic_plotting` should return an Altair Chart object"

# Test gic_plotting function can throws an error if the principal input is invalid
def test_gic_plotting_invalid_principal():
    for i in principal_invalid:
        with pytest.raises((ValueError, TypeError)):
            gic_plotting(i, None, term_lengths_valid)

# Test gic_plotting function can throws an error if the gic_rates input is invalid
def test_gic_plotting_invalid_gic_rates():
    for i in gic_rates_invalid:
        with pytest.raises((ValueError, TypeError)):
            gic_plotting(principal_valid, i, term_lengths_valid)

# Test gic_plotting function can throws an error if the term_lengths input is invalid
def test_gic_plotting_invalid_term_lengths():
    for i in term_lengths_invalid:
        with pytest.raises((ValueError, TypeError)):
            gic_plotting(principal_valid, gic_rates_valid, term_lengths_invalid)

# Test gic_plotting function can output non-empty Altair Chart
def test_gic_plotting_non_empty_chart():
    chart = gic_plotting(principal_valid, None, term_lengths_valid)
    assert chart.data.empty == False
    assert chart.data.interest.sum() > 0