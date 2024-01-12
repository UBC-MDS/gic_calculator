def gic_plotting(interests, term_lengths):
    """GIC interest plotting

    Generate, output and export a bar chart to visualize the interest(s) accrued after investment(s) in GIC (Guarenteed Investment
    Certificate) for comparison.

    Parameters
    ----------
    interests : list
        A list of the total interest accrued per each investment
    term_lengths : list
        A list of the term length (duration) per each investment. To be one of the following standard options:
        90, 180, 270, 1, 1.5, 2, 3, or 5 correspond to 90 days, 180 days, 270 days, 1 year, 1.5 years, 2 years, 
        3 years, 5 years.

    Returns
    -------
    altair.vegalite.v4.api.Chart
        An Altair Chart object representing the bar chart of total interest accrued per each investment

    Examples
    --------
    >>> from gic_calculator.gic_plotting import gic_plotting
    >>> gic_plotting(interests=[17.26, 96.16], term_lengths=[90, 180])
    """

    pass
