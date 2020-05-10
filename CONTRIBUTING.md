# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

* [Types of Contributions](#types-of-contributions)
* [Contributor Setup](#setting-up-the-code-for-local-development)
* [Contributor Guidelines](#contributor-guidelines)
* [Contributor Testing](#testing-with-nox)
* [Becoming a Core Committer](#becoming-a-core-committer)

## Types of Contributions

You can contribute in many ways:

### Report Bugs

Report bugs at [Github Issue Tracker](https://github.com/insspb/ikt/issues).

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* If you can, provide detailed steps to reproduce the bug.
* If you don't have steps to reproduce the bug, just note your observations in
as much detail as you can. Questions to start a discussion about the issue are
welcome.

### Fix Bugs

Bugs are usually marked with 'bug' label.

* Look through the GitHub issues for bugs and issues.
* Any bug or problem issue without WIP label or related pull requests is open
to whoever wants to implement it.
* If several fix approaches possible feel free to discuss possible fixes
before actual codding.

### Implement Features

Feature requests are usually marked with "enhancement" or "please-help" labels.

* Look through the GitHub issues for feature requests.
* Any feature request without WIP label or related pull requests is open to
whoever wants to implement it.
* Please do not combine multiple feature enhancements into a single pull
request.
* Feel free to create alternative features implementation if issue exist, but
related pull request not yet merged. Please discuss in original pull request
first.

### Write Documentation

Image Keyword Tool (IKT) could always use more documentation, whether as part of
the official IKT docs, in docstrings, or even on the web in blog posts,
articles, and such.

If you want to review your changes on the documentation locally, after
[Contributor Setup](#setting-up-the-code-for-local-development) you can
do:

```bash
nox -s docs
```

This will compile the documentation, open it in your browser and start watching
the files for changes, recompiling as you save.

### Submit Feedback

The best way to send feedback is to file an issue at
[Github Issue Tracker](https://github.com/insspb/ikt/issues).

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are
welcome :)

## Setting Up the Code for Local Development

Here's how to set up `ikt` for local development.

* Fork the `ikt` repo on GitHub.
* Clone your fork locally:

```bash
git clone git@github.com:your_name_here/ikt.git
```

* Install your local copy into a virtualenv. Assuming you have
venv installed, this is how you set up your fork for local development:

```bash
pip install -e .
```

* Install development tools and dependencies into same virtualenv.

```bash
pip install -r requirements.txt
```

* Configure pre-commit hooks automation for future git commits. More info at
[pre-commit documentation](https://pre-commit.com/)

```bash
pre-commit install
```

* Create a branch for local development:

```bash
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

* When you're done making changes, check that your changes pass the tests
and lint check:

```bash
nox
```

Please note that nox runs lint check automatically, since we have a test
environment for it. Linting is done with pre-commit verification, so it will
also correct some errors on this stage.

If you feel like running only the lint environment, please use the following
command:

```bash
nox -s linting
```

* Ensure that your feature or commit is fully covered by tests. Check report
after regular nox run.

You report will be placed to `htmlcov` directory. Please do not include this
directory to your commits. By default this directory in our `.gitignore` file.

* Commit your changes and push your branch to GitHub:

```bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

* Submit a pull request through the GitHub website.

## Contributor Guidelines

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
1. If the pull request adds functionality, the docs should be updated.
Put your new functionality into a function with a docstring, and add the feature
to the list in README.md.
1. The pull request must pass all CI/CD jobs before being ready for review.
1. If one CI/CD job is failing for unrelated reasons you may want to create
another PR to fix that first.

### Coding Standards

* PEP8
* Black formatting
* Docstrings required
* Try to use type annotations, if possible
* Write all code in Python 3.7+.
* Use f-strings

### Documentation Standards

* Markdown preferred over RST
* Line length: recommended 80 symbols, maximum 88, links are exceptions.
* Numbered lists preferred syntax use `1.` only.
* Unnumbered lists preferred syntax use `*`.

## Testing with nox

To run all tests using various versions of python in virtualenv defined in
`noxfile.py`, just run nox:

```bash
nox
```

This configuration file setup the pytest-cov plugin and it is an additional
dependency. It generate a coverage report after the tests.

It is possible to tests with pre-selected version of python, to do this the
command is:

```bash
nox -s tests-3.7 tests-3.8
```

Will run pytest with the python3.7 and python3.8 example.

[Nox](https://nox.thea.codes/) is new tool and in active development. Please
check nox documentation for last updates.

To list all available nox sessions and their status you can use:

```bash
nox -l
```

docs session is disabled for automatic run and intended only for interactive
launch for documentation development.

## Becoming a Core Committer

Contributors may be given core commit privileges.
Preference will be given to those with:

1. Past contributions to IKT and other open-source projects. Contributions to
IKT include both code (both accepted and pending) and friendly participation
in the issue tracker. Quantity and quality are considered.
1. A coding style that the other core committer find simple, minimal, and
clean.
1. Access to resources for cross-platform development and testing.
1. Time to devote to the project regularly.
