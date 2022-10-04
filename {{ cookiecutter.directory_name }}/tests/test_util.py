import os

from {{ cookiecutter.project_slug }}.util import get_version
from {{ cookiecutter.project_slug }}.util import render_latex

from .util import ASSETS_PATH


def test_get_version():
    version = get_version
    assert isinstance(version, str)
    assert version != ''


def test_render_latex():
    output_path = os.path.join(ASSETS_PATH, 'out.pdf')
    render_latex({'content': '$\pi = 3.141$'}, output_path)
    assert os.path.exists(output_path)
