=========
History
=========

0.1.0 (25.09.2022)
------------------

- Initial commit

0.2.0 (10.04.2022)
------------------

- Changed the local Poetry_ configuration in ``poetry.toml`` so that it does not create a separate
  virtualenv by itself and instead uses an already existing virtualenv.
- Added the instructions for an initial virtualenv setup to the ``DEVELOP.rst`` file.
- Fixed some issues with the include statements in ``pyproject.toml``.
    - I learned that the ``tests`` folder should *not* be included.
- Fixed some other templating issues in ``pyproject.toml``
- Added cookiecutter tests in the ``tests/test_cookiecutter.py`` file, using the plugins
  ``pytest.cookies`` and ``pytest.venv``.
- Extended the tests templating a bit by adding a ``tests/util.py`` and a ``tests/assets`` folder

0.2.1 (10.04.2022)
------------------

- Fixed a bug with the ``anon`` and ``de-anon`` commands where they would raise an exception for files with
  the wrong encoding. Now simply wrapped the corresponding section in a try-except
- Added a test case which executes the unittests of the actual bare-bones project folder.

0.3.0 (25.02.2023)
------------------

- Fixes the ``pyproject.toml`` to work with editable installs
- Added new templates for more advanced experiment inheritance

0.4.0 (28.04.2023)
------------------

- Changed the ``pycomex`` version dependency
- Now using the pycomex functional API everywhere
- Added some utility functions

0.5.0 (30.10.2023)
------------------

- no entry

0.6.0 (30.06.2025)
------------------

- Using `uv` as the package manager instead of `poetry`
- Using `hatchling` as the build engine instead of `poetry`