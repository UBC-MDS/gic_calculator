from gic_calculator.interest_calculator import interest_calc

def calculate_gic_difference(term_length_n1, term_length_n2, principal, interest_rate1=None, interest_rate2=None):

    """
    Calculate and return the difference in total returns between two GIC (Guaranteed Investment Certificate) investment periods.

    This function computes the total returns (both interest and principal) for two distinct GIC investment periods,
    using different or identical annual interest rates for each period. It then calculates the difference in these total
    returns, effectively comparing the profitability of the two investment periods.

    Parameters:
    ----------    
    term_length_n1 : int 
        The duration in days or years of the first investment period. A list of the term length (duration) per each investment. 
        To be one of the following standard options: 
        90, 180, 270, 1, 1.5, 2, 3, or 5 correspond to 90 days, 180 days, 270 days, 1 year, 1.5 years, 2 years, 3 years, 5 years.
    term_length_n2 : int
        The duration in days or years of the second investment period. A list of the term length (duration) per each investment. 
        To be one of the following standard options:
        90, 180, 270, 1, 1.5, 2, 3, or 5 correspond to 90 days, 180 days, 270 days, 1 year, 1.5 years, 2 years, 3 years, 5 years.
    principal : float
        The initial amount of money invested in both periods.
    interest_rate1 : float, optional
        Annual interest rate (in percentage) for the first period. If not provided, a default value defined in `interest_calc` is used.
    interest_rate2 : float, optional 
        Annual interest rate (in percentage) for the second period. If not provided, it assumes the same rate as interest_rate1 or the 
        default from `interest_calc`.

    Returns:
    ----------
    float : 
        The difference in the total returns (sum of interest and principal) between the two investment periods.

    Example:
    ----------
    >>> difference = calculate_gic_difference(5, 10, 1000, 2.5, 3.0)
    >>> print(f"Difference in GIC returns between 5 and 10 years: ${difference:.2f}")
    """

     # Test if the inputs are numeric
    if not (isinstance(term_length_n1, (int, float)) and
            isinstance(term_length_n2, (int, float)) and
            isinstance(principal, (int, float)) and
            (interest_rate1 is None or isinstance(interest_rate1, (int, float))) and
            (interest_rate2 is None or isinstance(interest_rate2, (int, float)))):
        raise TypeError("term_length and principal must be entered as numeric values. gic_rate must be numeric or None type.")
  
    # Test if the term_length is in the allowable range
    if term_length_n1  not in [90, 180, 270, 1, 1.5, 2, 3, 5]:
        raise ValueError("term_length must be provided as one of the following values 90, 180, 270, 1, 1.5, 2, 3, 5.")
    if term_length_n2  not in [90, 180, 270, 1, 1.5, 2, 3, 5]:
        raise ValueError("term_length must be provided as one of the following values 90, 180, 270, 1, 1.5, 2, 3, 5.")
    
    # Test if the principal is non-negative
    if principal < 0:
        raise ValueError("principal must be entered as a postive numeric value.")
    
    # Calculate interest for both periods
    interest_n1 = interest_calc(principal, term_length_n1, interest_rate1)[1]
    interest_n2 = interest_calc(principal, term_length_n2, interest_rate2)[1]

    # Calculate total returns for both periods
    total_n1 = principal + interest_n1
    total_n2 = principal + interest_n2

    # Calculate the difference in returns
    return_difference = total_n2 - total_n1


    return round(return_difference, 2)

