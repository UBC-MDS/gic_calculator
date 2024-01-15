def total_gic(principal, interest):
    """
    Calculate the total amount for a Guaranteed Investment Certificate (GIC) after n years.

    This function computes the total amount by adding the pre-calculated interest to the principal amount.
    It assumes that the interest has been calculated separately over a certain number of years.

    Parameters:
    principal (float): The initial amount of money invested in the GIC.
    interest (float): The total interest earned over the investment period.

    Returns:
    float: The total amount after the investment period, which is the sum of the principal and interest.

    Example:
    principal_amount = 1000.0  
    accumulated_interest = 200.0  # Replace with the calculated interest
    total_amount = total_gic(principal_amount, accumulated_interest)
    print(f"Total amount after adding interest: ${total_amount:.2f}")
    """

    # Calculate the total amount
    total_amount = principal + interest

    return total_amount
