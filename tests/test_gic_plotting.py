from gic_calculator.gic_plotting import gic_plotting
import pytest

principal_valid = 1000.0
gic_rates_valid = [1.0, 2.1]
term_lengths_valid = [90, 1.5]

principal_invalid = ['string', -1000, 0]
gic_rates_invalid = ['string', 1.0, [], [1.0, 2.1, 3.2]]
term_lengths_invalid = ['string', 1.5, [], [90, 1, 270]]

# Test gic_plotting function can output Altair Chart with valid inputs
def test_gic_plotting_valid_inputs():
    assert isinstance(gic_plotting(principal_valid, term_lengths_valid, None), alt.Chart), "`gic_plotting` should return an Altair Chart object"
    assert isinstance(gic_plotting(principal_valid, term_lengths_valid, gic_rates_valid), alt.Chart), "`gic_plotting` should return an Altair Chart object"

# Test gic_plotting function can throws an error if the principal input is invalid
def test_gic_plotting_invalid_principal():
    for i in principal_invalid:
        with pytest.raises((ValueError, TypeError)):
            gic_plotting(i, term_lengths_valid, None)

# Test gic_plotting function can throws an error if the gic_rates input is invalid
def test_gic_plotting_invalid_gic_rates():
    for i in gic_rates_invalid:
        with pytest.raises((ValueError, TypeError)):
            gic_plotting(principal_valid, term_lengths_valid, i)

# Test gic_plotting function can throws an error if the term_lengths input is invalid
def test_gic_plotting_invalid_term_lengths():
    for i in term_lengths_invalid:
        with pytest.raises((ValueError, TypeError)):
            gic_plotting(principal_valid, term_lengths_invalid, gic_rates_valid)

# Test gic_plotting function can output non-empty Altair Chart
def test_gic_plotting_non_empty_chart():
    chart = gic_plotting(principal_valid, term_lengths_valid, None)
    assert chart.data.empty == False
    assert chart.data.interest.sum() > 0