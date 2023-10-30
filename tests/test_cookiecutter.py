import os
from pytest_venv import VirtualEnvironment

from .util import PATH, PROJECT_PATH
from .util import run_command
from .util import prepare_poetry


def test_bake(cookies):
    """
    Tests if the cookiecutter command basically runs without error and whether all files are present in the
    final folder
    """
    context = {
        'directory_name': 'compex',
        'project_slug': 'compex',
        'version': '0.2.0'
    }
    result = cookies.bake(template=PROJECT_PATH, extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None

    files = os.listdir(result.project_path)
    expected_files = ['README.rst', 'DEVELOP.rst', 'pyproject.toml', 'poetry.toml', 'tests', 'compex']
    for file_name in expected_files:
        assert file_name in files

    package_path = os.path.join(result.project_path, 'compex')
    files = os.listdir(package_path)
    expected_files = ['VERSION', 'utils.py', 'cli.py', 'templates', 'experiments']
    for file_name in expected_files:
        assert file_name in files


def test_cli(cookies, venv):
    context = {
        'directory_name': 'compex',
        'project_slug': 'compex',
        'version': '0.3.0'
    }
    result = cookies.bake(template=PROJECT_PATH, extra_context=context)

    # Here we install the now templated version of this folder via pip
    venv.install(f'{result.project_path}')
    # One way we can immediately test whether it worked is by trying to import our package in python
    python_command = f'{venv.python} -c "import compex"'
    proc, out, err = run_command(python_command)
    assert proc.returncode == 0

    # ~ TESTING CLI
    # The pip installation should have also created a binary file that we can use to invoke the command line
    # interface of our application. This file should exist and we should be able to execute it
    cli_path = os.path.join(venv.bin, 'compex')
    assert os.path.exists(cli_path) and os.path.isfile(cli_path)
    cli_command = f'{cli_path} --help'
    proc, out, err = run_command(cli_command)
    print('out', out)
    print('err', err)
    assert proc.returncode == 0
    assert out != ''

    # The version command should work right out the box and should return the correct version we have
    # specified above in the context
    version_command = f'{cli_path} --version'
    proc, out, err = run_command(version_command)
    assert proc.returncode == 0
    assert '0.3.0' in out


def test_installation(cookies, venv):
    """
    Tests if the pip installation of the bare-bones project works. Also tests for example if the
    installation of the command line interface works properly
    """
    context = {
        'directory_name': 'compex',
        'project_slug': 'compex',
        'version': '0.3.0'
    }
    result = cookies.bake(template=PROJECT_PATH, extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None

    # Here we install the now templated version of this folder via pip
    venv.install(f'{result.project_path}')
    # One way we can immediately test whether it worked is by trying to import our package in python
    python_command = f'{venv.python} -c "import compex"'
    proc, out, err = run_command(python_command)
    assert proc.returncode == 0


def test_poetry(cookies, venv):
    context = {
        'directory_name': 'compex',
        'project_slug': 'compex',
        'version': '0.3.0'
    }
    result = cookies.bake(template=PROJECT_PATH, extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None

    # First of all we need to install poetry into the venv
    venv.install('poetry==1.2.1')
    poetry_path = f'{venv.python} -m poetry'

    # and we also need to make sure to switch to the correct environment
    env_command = f'{poetry_path} -vvv env use {venv.python}'
    proc, out, err = run_command(env_command, cwd=result.project_path)
    # Then we need to run "poetry install"
    install_command = f'{poetry_path} --no-cache install'
    proc, out, err = run_command(install_command, cwd=result.project_path)
    assert proc.returncode == 0
    assert 'No dependencies to install or update' not in out

    # We can check if that worked by attempting to import "click" first (which is a dependency of our
    # project and thus should have been installed and then also attempting to install our project itself
    proc, out, err = run_command(f'{venv.python} -c "import click"')
    assert proc.returncode == 0
    proc, out, err = run_command(f'{venv.python} -c "import compex"')
    assert proc.returncode == 0

    # Now another thingy we can test is if the poetry bumpversion feature works
    bumpversion_command = f'{poetry_path} version minor'
    proc, out, err = run_command(bumpversion_command, cwd=result.project_path)
    assert proc.returncode == 0
    proc, out, err = run_command(install_command, cwd=result.project_path)
    assert proc.returncode == 0

    cli_path = os.path.join(venv.bin, 'compex')
    assert os.path.exists(cli_path)
    version_command = f'{cli_path} --version'
    proc, out, err = run_command(version_command)
    assert proc.returncode == 0
    assert '0.4.0' in out


def test_testing(cookies, venv):
    context = {
        'directory_name': 'compex',
        'project_slug': 'compex',
        'version': '0.3.0'
    }
    result = cookies.bake(template=PROJECT_PATH, extra_context=context)
    poetry, path = prepare_poetry(result.project_path, venv)

    # First we check if pytest is even available for the venv binary
    pytest_command = f'{venv.python} -c "import pytest"'
    proc, out, err = run_command(pytest_command)
    assert proc.returncode == 0

    # Then we can actually run pytest for the tests inside the project folder
    tests_path = os.path.join(path, 'tests')
    test_command = f'{venv.python} -m pytest -s {tests_path}'
    proc, out, err = run_command(test_command)
    assert proc.returncode == 0
