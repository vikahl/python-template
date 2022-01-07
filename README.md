# A reasonable modern Python cookiecutter

A reasonable modern Python cookiecutter with support for libraries, clis and
services.

_Not everything needs to be the fanciest and shiniest, sometimes it is better
to use reasonable modern tools that will not change and fit into existing
systems._

A generated example can be found at https://github.com/vikahl/python-example

## Basic ideas

- Always package the Python code as a library, even if is a service that will
  not be distributed through PyPI. Doing this makes it easy to write tests or
  extend functionality in various directions.
- Use [Setuptools] as the build system. It is a proven build system that has
  gotten much better with the static configuration files (`setup.cfg`) and PEP
  517 compliant builds. I do not see a reason to use another system.
- Use Github Actions to run tests configured in tox and build and upload to
  PyPI for libraries.
- Selection for library, cli and/or service support.

## Template settings

- __project_name__: Human friendly name for the project.
- __description__: Short description of the project. Added to the README and
  package.
- __module_name__: Project name, following specification in [PEP 508]. Will be
  suggested based on the project name.
- __author__: Name of the project author. Added in package metadata (setup.cfg)
  and in some cases the license.
- __email__: Email for the project author. Added in package metadata (setup.cfg).
- __homepage__: Homepage for the project. Added in package metadata (setup.cfg).
- __license__: Select a license for the project. Will add a trove classifier
  (in setup.cfg) and a license file. If another license is needed they can be
  replaced later.
- __version__: Initial version.
- __min_python__: Minimum Python version that is supported. Tox will generate
  test environments for all newer versions. Backported modules might be used
  for older Python versions.
- __library__: Toggle library functions, adds a Github workflow for uploading
  to PyPi.
- __cli__: Toggle cli functions, adds a basic cli (based on Typer) with
  entrypoint defined in setup.cfg.
- __service__: Toggle service functions, adds a dockerfile and instructions on
  compiled requirements.

## Linters and tools

_A note about configs_: This template aims to collect all configuration in
`pyproject.toml`, except for Setuptools which uses `setup.cfg` and tox which
uses `tox.ini` (until tox better supports pyproject.toml).

The linters and formatters are configured in tox and can be invoked by running
`tox`. Github Actions ensures the same linters and formatters are run in CI.

- [Setuptools]: Packaging tool. Uses `setup.cfg` for package configuration.
- [tox](https://tox.wiki/en/latest/): Test automation framework. Run in Github
  actions and can be run locally.
- [Black](https://github.com/psf/black): Code formatter, formats the code in a
  consistent way. No special config.
- [Isort](https://pycqa.github.io/isort/): Formats import statement to keep
  them consistent and tidy. Minimal config in `pyproject.toml` to be compatible
  with Black.
- [Pylint](https://pylint.org/): Linter. Although a bit noisy it catches many
  common mistake. Configured in `pyproject.toml`.
- [Mypy](http://www.mypy-lang.org/): Type checker. Configured in
  `pyproject.toml`.
- [Pytest](https://docs.pytest.org/en/latest/): Python testing framework. Used
  for the tests.
- [Pytest-cov](https://github.com/pytest-dev/pytest-cov): Pytest plugin to
  measure code coverage.
- [Pip-tools](https://github.com/jazzband/pip-tools/) (service only): Used to
  compile requirements for the service.

## Questions, comments or thoughts

File an issue!

<!-- Links -->
[Setuptools]: https://setuptools.pypa.io/
[PEP 508]: https://www.python.org/dev/peps/pep-0508/#names
