# gic_calculator

## Summary

### Project Summary
This project involves developing a Python package designed to assist users in understanding and analyzing the financial returns from Guaranteed Investment Certificates (GICs). The package focuses on calculating the interest returns over different investment periods, comparing these returns, and providing a visual representation of the differences. This utility will be particularly useful for investors and financial advisors who need to make informed decisions regarding GIC investments.

### Functions Included in the Package
(1) interest_calc(principal, term_length, gic_rate=None)

Description: Calculates the interest earned on a GIC after a specified number of years.
Inputs: principal amount, term length of investment and GIC rate.

(2) calculate_gic_difference(n1_year, n2_year, principal, interest_rate)

Description: Calculates the difference in total returns (interest + principal) of a GIC between two different investment periods.
Functionality: Utilizes the interest_calc function to determine the interest for two different periods and then finds the difference.

(3) total_gic(principal, interest):

Description: Calculates the total amount for a Guaranteed Investment Certificate (GIC) after a specified number of years.
Functionality: Utilizes the interest_calc function to determine the total amount for two different periods.

(4) gic_plotting(interests, term_lengths)

Description: Generates a bar plot to visually represent the difference in returns as calculated by calculate_gic_difference.
Purpose: Helps users to easily visualize and understand the financial impact of investing for different durations.


### Fit into the Python Ecosystem

There are several Python packages focused on financial calculations and investment analysis, such as numpy-financial or pandas, which are used for a wide range of financial computations and data analysis. However, a specialized package focusing exclusively on GIC investment analysis, particularly one that compares returns over different investment periods and visualizes these comparisons appears to be unique. This package would thus fill a niche for those specifically interested in GIC investments.

By providing targeted functionality, the proposed package offers a more user-friendly and focused approach for individuals specifically dealing with GIC investments, setting it apart from more general financial analysis tools.

## Contributors

`gic_calculator` was created by Angela Chen (@angelachenmo), Tony Shum(@tonyshumlh), Ruocong Sun (@sungg888), Alysen Townsley (@AlysenTownsley).


## Usage

```bash
$ pip install gic_calculator
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`gic_calculator` is licensed under the terms of the MIT license.

## Credits

`gic_calculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
