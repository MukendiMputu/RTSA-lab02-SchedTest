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

#The necessary Test for the Liu and Layland Bound
def test(tasks):
    n = tasks.shape[0]
    U = TH.getTotalUtilization(tasks=tasks, NrTasks=n)
    U_lub = n * ((2 ** (1 / n)) - 1)
    
    # for fewer tasks than 10, we use the exact computed least upper bound
   #  if n < 10:
   #     return U <= U_lub

    # from 10 tasks up unlimited, we use the limes of n(2 ** 1/n - 1)
    return U <= U_lub # np.log(2) 

