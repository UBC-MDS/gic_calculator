import altair as alt
import pandas as pd
from gic_calculator.interest_calculator import interest_calc

def gic_plotting(principal, term_lengths, gic_rates=None):
    """GIC interest plotting

    Generate, output and export a bar chart to visualize the interest(s) accrued after investment(s) in GIC (Guarenteed Investment
    Certificate) for comparison.

    Parameters
    ----------
    principal : float
        The principal (initial amount) to be invested in the GIC account.
    term_lengths : list
        A list of the term length (duration) per each investment. To be one of the following standard options:
        90, 180, 270, 1, 1.5, 2, 3, or 5 correspond to 90 days, 180 days, 270 days, 1 year, 1.5 years, 2 years, 
        3 years, 5 years.
    gic_rates : list, optional
        A list of the GIC rate for the term length and investment type (fixed / cashable). This information
        can be found on your bank's website. If a value is not provided by the user, default values 
        will be used based on the specifed term length, as follows (GIC rates have units of percent): 
        90 days = 1.40, 180 days = 3.90, 270 days = 5.10, 1 year = 4.90, 1.5 years = 4.80,
        2 years = 4.10, 3 years = 4.00, 5 years = 3.75.

    Returns
    -------
    altair.vegalite.v4.api.Chart
        An Altair Chart object representing the bar chart of total interest accrued per each investment

    Examples
    --------
    >>> from gic_calculator.gic_plotting import gic_plotting
    >>> gic_plotting(interests=[17.26, 96.16], term_lengths=[90, 180])
    """

    # Test function inputs 
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

    # Define a dictionary of the units of the term_length
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

    # Obtain interest rates and interests
    n = len(term_lengths)
    interests = []
    title = []

    for i in range(n):
        if gic_rates is None:
            rate, interest = interest_calc(principal, term_lengths[i])
        else:
            rate, interest = interest_calc(principal, term_lengths[i], gic_rates[i])

        interests.append(interest)
        title.append(f"""In {term_lengths[i]} {default_info[term_lengths[i]]['unit']}, at an interest rate of {rate:.2f}%, \
you'll have earned ${interest:.2f} in interest.""")

    # Create the bar chart of the 2 investments
    term_lengths_str = [str(i+1) + ') ' + str(term) + ' ' + default_info[term]['unit'] for i, term in enumerate(term_lengths)]

    plot_df = pd.DataFrame({'term_length': term_lengths_str, 'interest': interests})
    chart = alt.Chart(
        plot_df, 
        width=alt.Step(200),
        title=alt.Title(title)
    ).mark_bar().encode(
        x=alt.X('term_length').title('GIC Term'),
        y=alt.Y('interest').axis(format='$~s').title('Interest Earned'),
        color=alt.value('orange')
    ).configure_scale(
        bandPaddingInner=0.5
    )

    return chart
