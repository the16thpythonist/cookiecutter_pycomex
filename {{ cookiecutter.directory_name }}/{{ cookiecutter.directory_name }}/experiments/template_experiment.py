"""
This string will be saved to the experiment's archive folder as the "experiment description"

CHANGELOG

0.1.0 - initial version
"""
import os
import pathlib

import numpy as np
import matplotlib.pyplot as plt

from pycomex.experiment import Experiment
from pycomex.util import Skippable

PATH = pathlib.Path(__file__).parent.absolute()

SHORT_DESCRIPTION = (
    'This will be the short description when listing the experiments from the command line'
)

# == EXPERIMENT PARAMETERS ==
BASE_PATH = PATH
NAMESPACE = 'results/template'
DEBUG = True
with Skippable(), (e := Experiment(BASE_PATH, NAMESPACE, globals())):
    # "e.info" should be used instead of "print". It will use python's "logging" module to not only
    # print the content ot the console but also write it into a log file at the same time.
    e.info('starting experiment...')


# == ANALYSIS ==
with Skippable(), e.analysis:
    e.info('starting analysis...')
