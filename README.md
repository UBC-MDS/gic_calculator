# gic_calculator

[![ci-cd](https://github.com/UBC-MDS/gic_calculator/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/gic_calculator/actions/workflows/ci-cd.yml) [![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/) [![Documentation Status](https://readthedocs.org/projects/gic-calculator/badge?version=latest)](https://gic-calculator.readthedocs.io/en/latest/?badge=latest) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![version](https://img.shields.io/github/v/release/UBC-MDS/gic_calculator) ![release](https://img.shields.io/github/release-date/UBC-MDS/gic_calculator) [![codecov](https://codecov.io/gh/UBC-MDS/gic_calculator/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/gic_calculator)

## Summary

### Project Summary

This project involves developing a Python package designed to assist users in understanding and analyzing the financial returns from Guaranteed Investment Certificates (GICs). This [`link`](https://www.td.com/ca/en/personal-banking/personal-investing/products/gic/what-is-a-gic) explains what a GIC is in more detail. The package focuses on calculating the interest returns over different investment periods, comparing these returns, and providing a visual representation of the differences. This utility will be particularly useful for investors and financial advisors who need to make informed decisions regarding GIC investments.

Website: [`https://gic-calculator.readthedocs.io/en/latest/`](https://gic-calculator.readthedocs.io/en/latest/?badge=latest)

### Functions Included in the Package

`interest_calc(principal, term_length, gic_rate=None)`: Calculates the interest earned on a GIC after a specified number of years.

`calculate_gic_difference(term_length_n1, term_length_n2, principal, interest_rate1=None, interest_rate2=None)`: Calculates the difference in total returns (interest + principal) of a GIC between two different investment periods.

`gic_plotting(principal, term_lengths, gic_rates=None)`: Generates a bar plot to visually represent the difference in returns as calculated by `interest_calc`.

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

`gic_calculator` can be used to calculate interest accrual on a GIC of varying term lengths or GIC rates, as follows: 

```
from gic_calculator.interest_calculator import interest_calc
interest_calc(5000, 1)
interest_calc(5000, 1, 5.5)
```

`gic_calculator` can be used to calculate the difference in total return (interest + principal) of a GIC between two different investment periods, as follows: 

```
from gic_calculator.gic_difference import calculate_gic_difference
calculate_gic_difference(1, 3, 5000)
calculate_gic_difference(1, 3, 5000, 5.5, 3.5)
```

`gic_calculator` can be used to create a bar plot to visually represent the difference in returns as calculated by `interest_calc`, as follows: 

```
from gic_calculator.gic_plotting import gic_plotting
gic_plotting(5000, [1, 3])
```

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

## References

1. Jacob VanderPlas, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben Welsh, and Scott Sievert. Altair: interactive statistical visualizations for python. Journal of open source software, 3(32):1057, 2018.
2. Guido Van Rossum and Fred L. Drake. Python 3 Reference Manual. CreateSpace, Scotts Valley, CA, 2009. ISBN 1441412697.
3. Krekel et al., pytest 7.4, 2004. [https://github.com/pytest-dev/pytest](https://github.com/pytest-dev/pytest)
4. TD Canada Trust. (n.d.). What is a GIC? Retrieved January 30, 2024, from [https://www.td.com/ca/en/personal-banking/personal-investing/products/gic/what-is-a-gic](https://www.td.com/ca/en/personal-banking/personal-investing/products/gic/what-is-a-gic)
5. UBC MDS. (n.d.). Collaborative Software Development Course Notes Retrieved from [https://pages.github.ubc.ca/MDS-2023-24/DSCI_524_collab-sw-dev_book/materials/lectures/](https://pages.github.ubc.ca/MDS-2023-24/DSCI_524_collab-sw-dev_book/README.html)
