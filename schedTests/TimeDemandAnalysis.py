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
    isSchedulable = True
    global set_num 
    set_num += 1

    print(f"\n======= TASK SET #{set_num} =======\n")
    # For each tasks in the ordered set
    for i in range(len(sortedtasks)):

        print(f'Task #{i} {tasks[i]}:')

        # calculate the time points for the demand function
        # t = j * P_k for k = 1, 2,...i and j = 1, 2,...,math.ceil(P_i / P_k)
        # list_of_t = [
        #    j * TH.P_i(sortedtasks, k)
        #    for k in range(i-1) 
        #    for j in range(1, int(math.ceil(TH.D_i(sortedtasks, i) / TH.P_i(sortedtasks, k))))
        #    ]
        # list_of_t = [TH.P_i(sortedtasks, k-1) for k in range(i+1)]
        list_of_t = []
        for k in range(i):
            list_of_t.append(TH.P_i(sortedtasks, k-1))

        print(f'\t list of t: {list_of_t}')

        # at any time t between 0 and and TH.P_i
        for j in range(len(list_of_t)):
        # for t in range(int(TH.C_i(sortedtasks, i)), int(TH.P_i(sortedtasks, i)+1), int(step)):

            # if the demand for CPU time of task i exceeds the available time t
            if time_demand_func(sortedtasks, i, list_of_t[j]) > list_of_t[j]:
                isSchedulable = False # then the task i will not meet its deadline, hence taskset not schedulable
            print(f'\t time-demand for t := {list_of_t[j]} ---> {time_demand_func(sortedtasks, i, list_of_t[j])}  is schedulable: {isSchedulable}')
    return isSchedulable


def time_demand_func(tasks, i, t):
    sum = 0
    for k in range(i-1):
        sum += math.ceil(t / TH.P_i(tasks, k)) * TH.C_i(tasks, k)
    return TH.C_i(tasks, i) + sum
