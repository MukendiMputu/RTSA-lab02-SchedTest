import numpy as np
import include.TasksHelper as TH

# The tasks is an Array with three columns and n Rows
# Each Row represents one Task
# The columns hold the Tasks parameters
# column 0 is period P,
# column 1 is deadline D
# column 2 is WCET C
# P_i is accessed as: tasks[i][0]
# D_i is accessed as: tasks[i][1]
# C_i is accessed as: tasks[i][2]
# The number of tasks can be accessed as: tasks.shape[0]


#The sufficient Test for the Hyperbolic bound
def test(tasks):
    """ The Hyperbolic bound is given as Π(U + 1) of all tasks: """
    # compute the hyperbolic bound as product of the U_factor of each task + 1
    hb = 1
    for i in range(tasks.shape[0]): # len(tasks) is 10
        hb *= (TH.C_i(tasks, i) / TH.P_i(tasks, i)) + 1
    # compare this computed bound to 2.0
    # if greater then no guaranty of schedulability
    # otherwise task set is schedulable
    return hb <= 2.0
