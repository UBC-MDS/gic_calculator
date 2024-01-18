def calculate_gic_difference(n1_year, n2_year, principal, interest_rate1=None, interest_rate2=None):
    """
    Calculate and return the difference in total returns between two GIC (Guaranteed Investment Certificate) investment periods.

    This function computes the total returns (both interest and principal) for two distinct GIC investment periods,
    using different or identical annual interest rates for each period. It then calculates the difference in these total
    returns, effectively comparing the profitability of the two investment durations.

    Parameters:
    ----------
    n1_year (int): The duration in years of the first investment period.
    n2_year (int): The duration in years of the second investment period.
    principal (float): The initial amount of money invested in both periods.
    interest_rate1 (float, optional): Annual interest rate (in percentage) for the first period. If not provided,
                                       a default value defined in `calculate_gic_interest` is used.
    interest_rate2 (float, optional): Annual interest rate (in percentage) for the second period. If not provided,
                                       it assumes the same rate as interest_rate1 or the default from `calculate_gic_interest`.

    Returns:
    ----------
    float: The difference in the total returns (sum of interest and principal) between the two investment periods.

    Example:
    ----------
    >>> difference = calculate_gic_difference(5, 10, 1000, 2.5, 3.0)
    >>> print(f"Difference in GIC returns between 5 and 10 years: ${difference:.2f}")
    """
    # Calculate interest for both periods
    interest_n1 = interest_calc(principal, n1_year, interest_rate1)[1]
    interest_n2 = interest_calc(principal, n2_year, interest_rate2)[1]

    # Calculate total returns for both periods
    total_n1 = principal + interest_n1
    total_n2 = principal + interest_n2

    # Calculate the difference in returns
    return_difference = total_n2 - total_n1

    return return_difference