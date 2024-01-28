# Contributing

Core Contributors: Tony Shum(@tonyshumlh), Ruocong Sun (@sungg888), Alysen Townsley (@AlysenTownsley)

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Open an Issue [here](https://github.com/UBC-MDS/gic_calculator/issues) and explain the following.
* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Open an Issue [here](https://github.com/UBC-MDS/gic_calculator/issues) and explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `gic_calculator` for local development.

1. Download a copy of `gic_calculator` locally.
2. Install `gic_calculator` using `poetry`:

    ```console
    $ poetry install
    ```

3. Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

4. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

5. Commit your changes and open a pull request.

1. Fork the convertempPy repo on GitHub.

2. Clone your fork locally:
    ```console
    $ git clone git@github.com:UBC-MDS/gic_calculator.git
    ```

3. Install your local copy with Poetry, this is how you set up your fork for local development:
    ```console
    $ cd gic_calculator/
    $ poetry install
    ```

4. Create a branch for local development:
    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the tests by running pytest
    ```console
    $ poetry run pytest
    ```

6. Commit your changes and push your branch to GitHub:
    ```console
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `gic_calculator` project is released with a
[Code of Conduct](CONDUCT.md). By contributing to this project you agree to abide by its terms.
