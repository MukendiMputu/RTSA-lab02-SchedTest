import numpy as np
import math
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

# The Time Demand Analysis Test
set_num = 0

def test(tasks):
    # Sorting Taskset by Period/Deadline
    # This makes implementing TDA a lot easier
    shape = tasks.shape
    sortedtasks = tasks[tasks[:, 0].argsort()]
    
    # For each tasks in the ordered set

    # calculate the time points for the demand function
    t_old = 10**-3
    i = 0

    while True:
        t_new = workload_func(sortedtasks, i, t_old)
        # if the workload of task i exceeds the deadline
        if t_new > TH.D_i(sortedtasks, i):
            return False # task not schedulable

        if t_new == t_old:
            i += 1
            t_old = 10**-3
            #  chech array out of bounds
            if i == len(sortedtasks):
                return True
        t_old = t_new
    


def workload_func(tasks, i, t):
    sum = 0
    for k in range(i):
        sum += math.ceil(t / TH.P_i(tasks, k)) * TH.C_i(tasks, k)
    return TH.C_i(tasks, i) + sum
