def calculate_gic_difference(n1_year, n2_year, principal, interest_rate):
    """
    Calculate the difference in total returns (interest + principal) of a GIC between two different investment periods.

    This function uses the calculate_gic_interest function to find the interest for two different investment periods
    and then calculates the difference in total returns (interest + principal).

    Parameters:
    n1_year (int): The number of years for the first investment period.
    n2_year (int): The number of years for the second investment period.
    principal (float): The initial amount of money invested.
    interest_rate (float): Annual interest rate in percentage.

    Returns:
    float: The difference in total returns (interest + principal) between the two investment periods.

    Example:
    difference = calculate_gic_difference(5, 10, 1000, 2.5)
    print(f"Difference in GIC returns between 5 and 10 years: ${difference:.2f}")

    """
    # Calculate interest for both periods
    interest_n1 = calculate_gic_interest(n1_year, principal, interest_rate)
    interest_n2 = calculate_gic_interest(n2_year, principal, interest_rate)

    # Calculate total returns for both periods
    total_n1 = principal + interest_n1
    total_n2 = principal + interest_n2

    # Calculate the difference in returns
    return_difference = total_n2 - total_n1

    return return_difference
