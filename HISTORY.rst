=========
History
=========

0.1.0 (2022-09-25)
------------------

- Initial commit

0.2.0 (2022-10-04)
------------------

- Changed the local Poetry_ configuration in ``poetry.toml`` so that it does not create a separate
  virtualenv by itself and instead uses an already existing virtualenv.
- Added the instructions for an initial virtualenv setup to the ``DEVELOP.rst`` file.
- Fixed some issues with the include statements in ``pyproject.toml``.
    - I learned that the ``tests`` folder should *not* be included.
- Fixed some other templating issues in ``pyproject.toml``
- Added cookiecutter tests in the ``tests/test_cookiecutter.py`` file, using the plugins
  ``pytest.cookies`` and ``pytest.venv``.
