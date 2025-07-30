=========================
📋 Development Cheatsheet
=========================

=======================
`uv` package management
=======================

This project is intended to use uv_ for package managment, however it also possible to use any other package 
management system such as `pip`, `conda` or `poetry`. The following instructions are for `uv`.

Installing `uv`
===============

If not already installed on your system, you can install `uv` using the following command:

.. code-block:: console

    curl -LsSf https://astral.sh/uv/install.sh | sh

Setting up virtualenv development environment
=============================================

As a next step you have to create a new virtual environment for the project. This can be done using the `uv venv` command.
The `--seed` option makes sure that the important core packages are installed into the venv right away and the 
python version for the venv can be specified using the `--python` option.

.. code-block:: console

    uv venv --seed --python=3.10

This will create a new virtual environment in the `.venv` folder of the project. You can activate it using the
following command:

.. code-block:: console

    uv venv activate

Installing dependencies
========================

To install the dependencies of the project as they are listed in the `pyproject.toml` file you can use the `uv sync` 
command like this in the root directory of the project:

.. code-block:: console

    uv sync

Alternatively you can also use the `uv pip` interface to install the package into the current virtual environment in 
editable mode:

.. code-block:: console

    uv pip install -e .


.. _Poetry: https://python-poetry.org/
.. _uv: https://docs.astral.sh/uv/getting-started/


Publishing the package to PyPI
==============================

Using the given project structure and the `uv` package manager it is also fairly easy to publish the package to PyPI, 
which will be explained in the following sections.

Bumping the version
-------------------

First of all you need to bump the version of the package which is configured to be possible with the `bump-my-version`
tool that can be installed like this:

.. code-block:: console

    uv tool install bump-my-version

You can then use the tool to either bump the major, minor or patch version of the package like this:

.. code-block:: console

    bump-my-version bump -v major
    bump-my-version bump -v minor
    bump-my-version bimp -v patch

Building the package
---------------------

After having incremented the version string, you can compile the new veresion of the package using the `uv build` command, 
which will create the zipped source distribution and the wheel in the `dist` folder of the project.

.. code-block:: console

    uv build

Publishing the package
-----------------------

To publish the package to PyPI you can use the `uv publish` command, which will automatically upload the new package version to PyPI.
.. code-block:: console

    uv publish --token='{your_api_token}'


===
Git
===

Add Remote Repository
=====================

It makes sense to directly supply a Github personal auth token when registering a new remote location for
the local repository, because that will remove any hassle with authentication when trying to push in the
future.

.. code-block:: shell

    git remote add origin https:://[github_username]:[github_token]@github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
    git push origin master


Create Anonymous Github Repository
==================================

Some journals / conferences use a double blind review process, which means that all aspects of a submission
need to be anonymized. This also includes the code that is submitted alongside the paper. This project
already implements the ``anon`` and ``de-anon`` commands which can be used to replace potentially identifying
information about the authors with random hashes.

But beyond the contents of the repository, the repository itself needs to be anonymous. This means you have
to create a new github account and create a new repository there.

To do this you can follow these steps:

**(1)** Create a `new gmail account`_

**(2)** Use that to create a `new github account`_ as well

**(3)** Make sure to retrieve a personal access token for that account from the github developer settings

**(4)** Setup a new remote location for your local repository

.. code-block:: shell

    git remote add anon https://[username]:[access_token]@github.com/[username]/{{ cookiecutter.project_slug }}.git

**(5)** Create a new *orphan* branch and push to the repo

.. code-block:: shell

    git checkout -b --orphan anon
    git commit -a -m "anon"
    git push anon anon


.. _new gmail account: https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp
.. _new github account: https://github.com/join
