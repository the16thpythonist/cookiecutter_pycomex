"""
This is a sub experiment derived from ...

CHANGELOG

0.1.0 - initial version
"""
import os
import pathlib

from pycomex.experiment import SubExperiment
from pycomex.util import Skippable

PATH = pathlib.Path(__file__).parent.absolute()

# == EXPERIMENT PARAMETERS ==
EXPERIMENT_PATH = os.path.join(PATH, 'template_experiment.py')
BASE_PATH = PATH
NAMESPACE = 'results/template'
DEBUG = True
with Skippable(), (se := SubExperiment(EXPERIMENT_PATH, BASE_PATH, NAMESPACE, globals())):

    @se.hook('end_experiment')
    def hook(e):
        e.info('adding additional implementations to the end of the experiment...')
