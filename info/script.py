import os
import sys
import subprocess
from gathering import *



def run_all_opts(filename, heuristic):
    print("\nRunning all optimisations")
    data_file = open(filename, "w")
    data_file.write("Parameter file, Time taken, Solver nodes, Optimisation flag, Heuristic\n")
    data_file.flush()
    data_time = {}
    data_nodes = {}
    
    i = 0
    optimisations = ["-O0", "-O1", "-O2", "-O3"]
    for opt_flag in optimisations:
        #times,nodes = get_data(opt_flag)
        times,nodes = write_data(data_file, opt_flag, heuristic=heuristic)
        data_time[opt_flag] = times
        data_nodes[opt_flag] = nodes

    print_data(data_time, data_nodes)



def run_no_opts(filename, heuristic):
    print("\nRunning default")
    data_file = open(filename, "w")
    data_file.write("Parameter file, Time taken, Solver nodes, Optimisation flag, Heuristic\n")
    data_file.flush()

    #times,nodes = write_data(data_file, opt_flag="", heuristic=heuristic)
    times,nodes = get_data("")

    print_timenodes(times, nodes)
    print_data({"Time": times}, {"Nodes": nodes})
    

# Run all params

# Clean up old info files
subprocess.run(["sh", "clean.sh"])


print("Gather data")
filepath = "/cs/home/sy35/Documents/cs4402/s1/Bombastic/data/"
filename_no_opts = sys.argv[1]
filename_all_opts = sys.argv[2]
heuristic = ""

#run_no_opts(filepath + filename_no_opts, heuristic)
run_all_opts(filepath + filename_all_opts, heuristic)

'''
run_no_opts("", "")
run_all_opts("", "")
'''
