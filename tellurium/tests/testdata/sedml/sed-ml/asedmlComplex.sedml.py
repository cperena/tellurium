"""
    tellurium 1.3.1

    auto-generated code (2016-02-26T09:10:17)
        sedmlDoc: L1V1          workingDir: /home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sed-ml
        inputType: SEDML_FILE

"""
from __future__ import print_function, division
import tellurium as te
import numpy as np
import matplotlib.pyplot as plt
import libsedml
import os.path

workingDir = '/home/mkoenig/git/tellurium/tellurium/tests/testdata/sedml/sed-ml'

# --------------------------------------------------------
# Models
# --------------------------------------------------------
#  - Application0 (Application0)
#  - Application0_0 (Application0 modified)

# Model <Application0>
Application0 = te.loadSBMLModel(os.path.join(workingDir, '../models/asedmlComplex.xml'))

# Model <Application0_0>
#   Change: <libsedml.SedChangeAttribute; proxy of <Swig Object of type 'SedChangeAttribute_t *' at 0x7fece6f83f90> >
Application0_0 = te.loadSBMLModel(os.path.join(workingDir, '../models/asedmlComplex.xml'))
# /sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='s0'] 25.0
Application0_0['init([s0])'] = 25.0

# --------------------------------------------------------
# Tasks
# --------------------------------------------------------
#  - task_0_0 (task_0_0)
#  - repeatedTask_0_0 (repeatedTask_0_0)

# Task <task_0_0>
Application0_0.setIntegrator('cvode')
Application0_0.timeCourseSelections = []
task_0_0 = Application0_0.simulate(start=0.0, end=30.0, steps=1000)

# Task <repeatedTask_0_0>
__range = [5.0, 10.0, 15.0]
repeatedTask_0_0 = [None] * len(__range)
for k, value in enumerate(__range):
    Application0_0.reset()
    Application0_0['init([s1])'] = value
    Application0_0.setIntegrator('cvode')
    Application0_0.timeCourseSelections = []
    repeatedTask_0_0[k] = Application0_0.simulate(start=0.0, end=30.0, steps=1000)

# --------------------------------------------------------
# DataGenerators
# --------------------------------------------------------
#  - time_repeatedTask_0_0 (time_repeatedTask_0_0)
#  - dataGen_repeatedTask_0_0_s0 (dataGen_repeatedTask_0_0_s0)
#  - dataGen_repeatedTask_0_0_s1 (dataGen_repeatedTask_0_0_s1)

# DataGenerator <time_repeatedTask_0_0>

# DataGenerator <dataGen_repeatedTask_0_0_s0>

# DataGenerator <dataGen_repeatedTask_0_0_s1>

# --------------------------------------------------------
# Outputs
# --------------------------------------------------------
#  - plot2d_Simulation1 (Application0plots)

# Output <plot2d_Simulation1>

