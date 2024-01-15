import pytest
from src.gic_calculator import total_gic

class TestTotalGIC:

    def test_positive_interest(self):
        principal_amount = 1000.0
        accumulated_interest = 200.0
        assert total_gic(principal_amount, accumulated_interest) == 1200.0

    def test_zero_interest(self):
        principal_amount = 1500.0
        accumulated_interest = 0.0
        assert total_gic(principal_amount, accumulated_interest) == 1500.0

    def test_negative_interest(self):
        principal_amount = 2000.0
        accumulated_interest = -300.0
        with pytest.raises(ValueError, match="Interest cannot be negative"):
            total_gic(principal_amount, accumulated_interest)

    def test_large_values(self):
        principal_amount = 1e10  # 10 billion
        accumulated_interest = 5e8  # 500 million
        assert total_gic(principal_amount, accumulated_interest) == 1.05e10

    def test_float_precision(self):
        principal_amount = 1234.56789
        accumulated_interest = 987.65432
        assert total_gic(principal_amount, accumulated_interest) == 2222.22221

    def test_invalid_principal(self):
        principal_amount = "invalid_value"
        accumulated_interest = 300.0
        with pytest.raises(TypeError, match="Principal must be a float"):
            total_gic(principal_amount, accumulated_interest)

    def test_invalid_interest(self):
        principal_amount = 2500.0
        accumulated_interest = "invalid_value"
        with pytest.raises(TypeError, match="Interest must be a float"):
            total_gic(principal_amount, accumulated_interest)
