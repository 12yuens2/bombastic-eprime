import os
import subprocess



def run_savilerow(param_file, optimisation="-O2"):
    subprocess.run(["../../savilerow", "../Bombastic.eprime", "../params/" + param_file, "-run-solver", "-out-minion", param_file+".minion", "-out-solution", param_file+".solution", "-out-info", param_file+".info", optimisation])

# Run all params

param_times = {}

for param_file in os.listdir("../params"):
    
    run_savilerow(param_file)

    with open(param_file+".info") as info_file:
        solver_time = info_file.readline().strip()
        param_times[param_file] = float(solver_time.split(":")[1])

for key in sorted(param_times):
    print(key + ": " + str(param_times[key]))

    

# Read info files to get time taken


# Save data to file
