def interest_calc(principal, term_length, gic_rate=None):
    """GIC interest accrual calculator
    
    Calculator to determine the interest to be accrued after investment in a GIC (Guarenteed Investment
    Certificate) for a user-specifed term, principal amount and interest rate. The interest rate term is
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
    float
        Outputs the total interest accrued after the investment term as a number in the same currency 
        as the principal amount specified by the user. 

    Examples
    --------
    >>> function_name(5000, 180, 3.90)
    96.16
    """