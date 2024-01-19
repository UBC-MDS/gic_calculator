# gic_calculator

## Summary

### Project Summary
This project involves developing a Python package designed to assist users in understanding and analyzing the financial returns from Guaranteed Investment Certificates (GICs). The package focuses on calculating the interest returns over different investment periods, comparing these returns, and providing a visual representation of the differences. This utility will be particularly useful for investors and financial advisors who need to make informed decisions regarding GIC investments.

### Functions Included in the Package
(1) interest_calc(principal, term_length, gic_rate=None)

Description: Calculates the interest earned on a GIC after a specified number of years.

(2) calculate_gic_difference(term_length_n1, term_length_n2, principal, interest_rate1, interest_rate2)

Description: Calculates the difference in total returns (interest + principal) of a GIC between two different investment periods.

(3) gic_plotting(principal, term_lengths, gic_rates)

Description: Generates a bar plot to visually represent the difference in returns as calculated by interest_calc.

### Fit into the Python Ecosystem

There are several Python packages focused on financial calculations and investment analysis, such as numpy-financial or pandas, which are used for a wide range of financial computations and data analysis. However, a specialized package focusing exclusively on GIC investment analysis, particularly one that compares returns over different investment periods and visualizes these comparisons appears to be unique. This package would thus fill a niche for those specifically interested in GIC investments.

By providing targeted functionality, the proposed package offers a more user-friendly and focused approach for individuals specifically dealing with GIC investments, setting it apart from more general financial analysis tools.

## Contributors

`gic_calculator` was created by Tony Shum(@tonyshumlh), Ruocong Sun (@sungg888), Alysen Townsley (@AlysenTownsley).

## Installation

1.  Clone this GitHub repository down to your local computer.

2.  Create and activate a virtual environment using conda
```
$ conda create --name <your-env-name> python=3.9 poetry -y
$ conda activate <your-env-name>
```

3. Navigate to the root directory of the package and install the package
```
$ poetry install
```

## Usage


## Developer notes

#### Tests

We have included tests and test data for functions used in our analysis
in the `tests` folder. The test suite can be run at the root directory of the
project using the pytest command below:

```         
pytest tests/*
```


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`gic_calculator` is licensed under the terms of the MIT license.

## Credits

`gic_calculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
