import os
import subprocess
from gathering import *


# Run all params
data_time = {}
data_nodes = {}

# Clean up old info files
subprocess.run(["sh", "clean.sh"])



print("Gather data")

i = 0
optimisations = ["-O0", "-O1", "-O2", "-O3"]
for opt_flag in optimisations:
    param_times = {}

    times, nodes = get_data(opt_flag)

    data_time[opt_flag] = times
    data_nodes[opt_flag] = nodes
   

# Read info files to get time taken

# Save data to file
print_data(data_time, data_nodes)

'''
print("Time data")
for opt,data in data_time.items():
    print(opt)
    i = 0
    for param, time in zip(get_param_list(), data):
        if i % 2 == 0:
            print("(" + str(i) + "," + str(time) + ")", end=" ")
        i += 1
        
    i = 0
    for param, time in zip(get_param_list(), data):
        if i % 2 != 0:
            print("(" + str(i) + "," + str(time) + ")", end=" ")
        i += 1


print("Node data")
for opt,data in data_nodes.items():
    print(opt)
    i = 0
    for param, time in zip(get_param_list(), data):
        if i % 2 == 0:
            print("(" + str(i) + "," + str(time) + ")", end=" ")
        i += 1
        
    i = 0
    for param, time in zip(get_param_list(), data):
        if i % 2 != 0:
            print("(" + str(i) + "," + str(time) + ")", end=" ")
        i += 1
'''

