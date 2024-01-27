def interest_calc(principal, term_length, gic_rate=None):
    """GIC interest accrual calculator
    
    Calculator to determine the interest to be accrued after investment in a GIC (Guarenteed Investment
    Certificate) for a user-specifed term, principal amount and GIC rate. The interest rate term is
    optional and will be set to default values for the term length, in the case it is not specified by 
    the user. 

    This calculator can be used to evaluate the expected interest accrual after a specified term length, 
    principal amount, and GIC rate to aid in investment planning / calculation of expected returns.

    Parameters
    ----------
    principal : int
        The principal (initial amount) to be invested in the GIC account.
    term_length : int
        The term length (duration) of the investment. To be one of the following standard options:
        90 days, 180 days, 270 days, 1 year, 1.5 years, 2 years, 3 years, 5 years. Enter the input 
        as either 90, 180, 270, 1, 1.5, 2, 3, or 5. 
    gic_rate : float, optional
        The GIC rate for the term length and investment type (fixed / cashable). This information
        can be found on your bank's website. If a value is not provided by the user, default values 
        will be used based on the specifed term length, as follows (GIC rates have units of percent): 
        90 days = 1.40, 180 days = 3.90, 270 days = 5.10, 1 year = 4.90, 1.5 years = 4.80,
        2 years = 4.10, 3 years = 4.00, 5 years = 3.75.

    Returns
    -------
    gic_rate : float
        Outputs the gic_rate utilized in the interest accrual calculation as a numeric value.
    interest_return : float
        Outputs the total interest accrued after the investment term as a number in the same currency 
        as the principal amount specified by the user.

    Examples
    --------
    >>> interest_calc(5000, 180, 3.90)
    1.4, 96.16
    """
    # Test function inputs 

    # Test if the inputs are numeric
    if not (isinstance(term_length, (int, float)) and
            isinstance(principal, (int, float)) and
            (gic_rate is None or isinstance(gic_rate, (int, float)))):
        raise TypeError("term_length and principal must be entered as numeric values. gic_rate must be numeric or None type.")
    
    # Test if the term_length is in the allowable range
    if term_length not in [90, 180, 270, 1, 1.5, 2, 3, 5]:
        raise ValueError("term_length must be provided as one of the following values 90, 180, 270, 1, 1.5, 2, 3, 5.")
    
    # Test if the principal is non-negative
    if principal < 0:
        raise ValueError("principal must be entered as a postive numeric value.")
    
    # Define a dictionary of the default gic_rates, based on the desired term_length
    rate_dict = {90: 1.4,
                 180: 3.9,
                 270: 5.1,
                 1: 4.9,
                 1.5: 4.8,
                 2: 4.1,
                 3: 4.0,
                 5: 3.8}
    
    # Handle case where user specifies a GIC rate input
    if gic_rate is not None:
        
        # Test if the gic_rate is a realistic value
        if not 0 < gic_rate <= 7:
            raise ValueError("gic_rate must be entered as a realistic value between 0 and 7.")
                             
        if term_length in [90, 180, 270]:
            interest_return = principal * (1 + gic_rate/100) ** (term_length / 365) - principal
        elif term_length in [1, 1.5, 2, 3, 5]:
            interest_return = principal * (1 + gic_rate/100) ** (term_length) - principal

    # Handle the default GIC rate case
    if gic_rate is None:
        gic_rate = rate_dict[term_length]

        if term_length in [90, 180, 270]:
            interest_return = principal * (1 + gic_rate/100) ** (term_length / 365) - principal
        if term_length in [1, 1.5, 2, 3, 5]:
            interest_return = principal * (1 + gic_rate/100) ** (term_length) - principal
            

    return gic_rate, round(interest_return, 2)

