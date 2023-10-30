|made-with-python| |python-version| |version|

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. |python-version| image:: https://img.shields.io/badge/Python-3.8.0-green.svg
   :target: https://www.python.org/

.. |version| image:: https://img.shields.io/badge/version-0.5.0-orange.svg
   :target: https://www.python.org/

=============================================
🍪 Cookiecutter for Computational Experiments
=============================================

This is a cookiecutter which will template a python project structure that is specifically tailored for
conducting and managing computational experiments.

Automatically sets up a fully functional project structure for a python project that focuses on the 
implementation of computational experiments for computer science research in areas such as 
algorithm engineering, machine learning and data science.

===========
🔥 Features
===========

- *Ready to release.* The created project structure uses the Poetry_ build system such that the code can 
  easily be published as a standalone package to the python package index (PyPi)!
- *Experiment with ease.* The package comes with a pre-configured ``experiments`` folder which can be used 
  to start writing PyComex_ experiments right away!
  However, you don't have to use the framework. Although recommended, there is no hard requirement that forces 
  you to do so. 
- *Simple command line interface. * provides the starting point for a simple Click_ command line interface, which 
  is pre-configured to print the package version and to interacti with the pycomex experiment modules.
- *Test your code.* Pytest_ unittesting options will be pre-created as well.

=============
🚀 Quickstart
=============

First of all make sure that cookiecutter is installed in your local python environment

.. code-block:: console

   pip3 install cookiecutter

To create a new project using this template as the basis simply execute:

.. code-block:: shell

    cookiecutter https://github.com/the16thpythonist/comex_cookiecutter.git

The command will present a number of input prompts which will ask you to configure certain details of the repository such as 
the name and the 

==============================
🖊️ A note on naming convention
==============================

To ensure compatiblity with the current python package naming conventions, you should give your project (and thus the created folder) 
A name in *snake case* - meaning that the name should consist only of lower case ascii characters and underscores. Additionally try to 
keep the name as short and concise as possible, because you will end up writing that name a lot.

.. code-block:: bash

   # Avoid white spaces and numerals in the name
   2 Different Graph Neural Networks    # BAD
   two_gnns                             # GOOD

   # Avoid names that are too long and only use underscores for delimiting
   LARGE-LANGUAGE-Models-are-great      # BAD
   large_language_models_are_great      # GOOD
   great_llms                           # BETTER             

   # Also avoid generic names since they will most likely already be in use 
   # for a different existing package
   my_thesis                            # BAD
   vrp_algorithm_benchmark              # GOOD

=============================
📖 Documentation / Next Steps
=============================

For more information on the different parts of the package that have been set up, consult the ``DEVELOP.rst`` file that 
has been created within your new project folder!

.. _PyComex: https://github.com/the16thpythonist/pycomex
.. _Poetry: https://python-poetry.org
.. _Pytest: https://docs.pytest.org/en/7.4.x/
.. _Click: https://click.palletsprojects.com/