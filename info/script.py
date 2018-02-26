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

