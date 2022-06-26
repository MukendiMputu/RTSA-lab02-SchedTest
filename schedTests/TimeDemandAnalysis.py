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


def test(tasks):
    # Sorting Taskset by Period/Deadline
    # This makes implementing TDA a lot easier
    shape = tasks.shape
    sortedtasks = tasks[tasks[:, 0].argsort()]

    print("\n======= TASK SET =======")
    # For each tasks in the ordered set
    for i in range(len(sortedtasks)):

        print(f'Task #{i} {tasks[i]}:')

        # calculate the time points for the demand function
        # t = j * P_k for k = 1, 2,...i and j = 1, 2,...,math.ceil(P_i / P_k)
        list_of_t = [TH.P_i(sortedtasks, k) * j for k in range(1, i)
                     for j in range(1, int(np.ceil(TH.D_i(sortedtasks, i) / TH.P_i(sortedtasks, k))))]

        # print(f'\t list of ts: {list_of_t}')

        # at any time t between 0 and and TH.P_i
        for t in np.sort(list_of_t):
        # for t in range(TH.C_i(sortedtasks, i), TH.P_i(sortedtasks, i)+1, TH.P_i(sortedtasks, i)):

            print(f'\tTime-Demand for t ({t}): {time_demand_func(sortedtasks, i, t)} ')

            # if the demand for CPU time of task i exceeds the available time t
            if time_demand_func(sortedtasks, i, t) > t:
                return False # then the task i will not meet its deadline, hence taskset not schedulable
    return True


def time_demand_func(tasks, i, delta=0):
    sum = 0
    for k in range(1, i-1):
        sum += math.ceil(delta / TH.P_i(tasks, k)) * TH.C_i(tasks, k)
    return TH.C_i(tasks, i) + sum
