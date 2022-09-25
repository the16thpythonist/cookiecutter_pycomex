import os
import pathlib
import unittest

from {{ cookiecutter.project_slug }}.util import get_version
from {{ cookiecutter.project_slug }}.util import render_latex

TEST_PATH = pathlib.Path(__file__).parent.absolute()


class TestUtil(unittest.TestCase):

    def test_get_version(self):
        version = get_version()
        self.assertIsInstance(version, str)
        self.assertNotEqual('', version)
        self.assertNotEqual(' ', version)

    def test_render_latex(self):
        output_path = os.path.join(TEST_PATH, 'out.pdf')
        render_latex({'content': '$\pi = 3.141$'}, output_path)
        self.assertTrue(os.path.exists(output_path))
