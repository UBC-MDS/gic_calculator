def gic_plotting(principal, gic_rates=None, term_lengths):
    """GIC interest plotting

    Generate, output and export a bar chart to visualize the interest(s) accrued after investment(s) in GIC (Guarenteed Investment
    Certificate) for comparison.

    Parameters
    ----------
    principal : float
        The principal (initial amount) to be invested in the GIC account.
    gic_rates : list, optional
        A list of the GIC rate for the term length and investment type (fixed / cashable). This information
        can be found on your bank's website. If a value is not provided by the user, default values 
        will be used based on the specifed term length, as follows (GIC rates have units of percent): 
        90 days = 1.40, 180 days = 3.90, 270 days = 5.10, 1 year = 4.90, 1.5 years = 4.80,
        2 years = 4.10, 3 years = 4.00, 5 years = 3.75.
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

    import altairs as alt
    import pandas as pd

    if not isinstance(principal, float) and not isinstance(principal, int):
        raise TypeError("Principal should be a number.")
    elif principal <= 0:
        raise ValueError("Principal must be positive.")
    
    if not isinstance(gic_rates, list) and gic_rates is not None:
        raise TypeError("GIC rates should be a list of rates, or None.")
    elif isinstance(gic_rates, list) and len(gic_rates) != 2:
        raise ValueError("GIC rates should contain exactly 2 rates for 2 investments")

    if not isinstance(term_lengths, list):
        raise TypeError("Term lengths should be a list of investment durations")
    elif len(term_lengths) != 2:
        raise ValueError("Term lengths should contain exactly 2 terms for 2 investments")

    default_info = {
        90: {'unit': 'days'},
        180: {'unit': 'days'},
        270: {'unit': 'days'},
        1: {'unit': 'year'},
        1.5: {'unit': 'years'},
        2: {'unit': 'years'},
        3: {'unit': 'years'},
        5: {'unit': 'years'}
    }

    n = len(term_lengths)
    interests = []
    title = []

    for i in range(n):
        if gic_rates is None:
            interest, rate = interest_calc(principal, term_lengths[i])
        else:
            interest, rate = interest_calc(principal, term_lengths[i], gic_rates[i])

        interests.append(interest)
        title.append(f"""In {term_lengths[i]} {default_info[term_lengths[i]]['unit']}, at an interest rate of {rate}%, \
        you'll have earned ${interest} in interest.""")

    term_lengths_str = [str(i+1) + ') ' + str(term) + ' ' + default_info[term]['unit'] for i, term in enumerate(term_lengths)]

    plot_df = pd.DataFrame({'term_length': term_lengths_str, 'interest': interests})
    chart = alt.Chart(
        plot_df, 
        width=alt.Step(200),
        title=alt.Title(title)
    ).mark_bar().encode(
        x=alt.X('term_length').title('GIC Term'),
        y=alt.Y('interest').axis(format='$~').title('Interest Earned'),
        color=alt.value('orange')
    ).configure_scale(
        bandPaddingInner=0.5
    )

    return chart


# Test Case 1
# check term length is a list of size = 2
# check term length values are float
# check term length values are 1 of the available options
# check 1st term length != 2nd term length?

# Test Case 2
# check interest rate is a list of size = 2 or = None
# check interest rate value are float
# check interest rate are >= 0

# Test Case 3
# check interest size = 2 or = None
# check interest value are float
# check interest are >= 0

# Test Case 4
# check principal is float and > 0

# Test Case 5
# return a chart
# return a non-empty chart
## incorrect type of column value handling e.g. Investment 1, Investment 2
## Test for correct error handling for incorrect object type (not a pandas data frame)
