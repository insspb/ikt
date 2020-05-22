"""Nox tool configuration file.

Nox is Tox tool replacement.
"""
import nox


nox.options.keywords = "not docs"


def base_install(session):
    """Creates basic environment setup for tests and linting."""
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    return session


@nox.session(python=["3.7", "3.8"])
def tests(session):
    """Run test suite with pytest."""
    session = base_install(session)
    session.run("pytest", "--cov-report=html", "--cov-report=xml")


@nox.session(python="3.8")
def linting(session):
    """Launch linting locally."""
    session = base_install(session)
    session.run("pre-commit", "run", "-a")


@nox.session(python="3.8")
def docs(session):
    """Build the documentation."""
    session.run("rm", "-rf", "docs/_build", external=True)
    session.install("-r", "docs/requirements.txt")
    session.install(".")
    session.cd("docs")
    sphinx_args = ["-b", "html", "-W", "source", "build/html"]

    if not session.interactive:
        sphinx_cmd = "sphinx-build"
    else:
        sphinx_cmd = "sphinx-autobuild"
        sphinx_args.insert(0, "--open-browser")
        sphinx_args.insert(0, "..")
        sphinx_args.insert(0, "-z")

    session.run(sphinx_cmd, *sphinx_args)
