|made-with-python| |python-version| |version|

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. |python-version| image:: https://img.shields.io/badge/Python-3.8.0-green.svg
   :target: https://www.python.org/

.. |version| image:: https://img.shields.io/badge/version-0.2.0-orange.svg
   :target: https://www.python.org/

==========================================
Cookiecutter for Computational Experiments
==========================================

This is a cookiecutter which will template a python project structure that is specifically tailored for
conducting and managing computational experiments (which are eventually meant to be published as a
research paper).

Usage
=====

To create a new instance based on this template simply run:

.. code-block:: shell

    cookiecutter https://github.com/the16thpythonist/comex_cookiecutter.git


Command Line Interface
======================

The repository comes with a fully functional boilerplate command line interface. You can see what it has to
offer like this:

.. code-block:: shell

    python3 [your_dir_name]/[your_dir_name]/cli.py --help
