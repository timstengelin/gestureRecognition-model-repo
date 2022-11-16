####################################################################################################
# main.py
####################################################################################################

from setupModel.setupModel import setupModel
from recordDataset.recordDataset import recordDataset

task = ' '
while task not in 'srx':
    task = input('press key:\n(s) for setup model\n(r) for record dataset\n(x) for exit\n').lower()

if task == 's':
    setupModel()
elif task == 'r':
    recordDataset()