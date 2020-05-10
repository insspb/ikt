"""Nox tool configuration file.

Nox is Tox tool replacement.
"""
import nox


nox.options.keywords = "not docs"


@nox.session(python=["3.7", "3.8"])
def tests(session):
    """Run test suite with pytest."""
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    if session.python == "3.8":
        session.run("pytest", "--cov-report=html")
    else:
        session.run("pytest")


@nox.session(python="3.8")
def linting(session):
    """Launch linting locally."""
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
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
