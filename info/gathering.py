import os
import subprocess

PARAM_PATH = "../test/"

def get_param_list():
    params = []
    for param_file in os.listdir(PARAM_PATH):
        params.append(param_file)

    return sorted(params)
        

def run_savilerow(param_file, optimisation="-O2"):
    FNULL = open(os.devnull, "w")

    if len(optimisation) == 0:
        subprocess.run(["../../savilerow", "../Bombastic.eprime", PARAM_PATH + param_file, "-run-solver", "-out-minion", param_file+".minion", "-out-solution", param_file+".solution", "-out-info", param_file+".info"])
    else:
        subprocess.run(["../../savilerow", "../Bombastic.eprime", PARAM_PATH + param_file, "-run-solver", "-all-solutions", "-out-minion", param_file+".minion", "-out-solution", param_file+".solution", "-out-info", param_file+".info", optimisation])



def get_data(opt_flag="-O2"):
    data_time = []
    data_nodes = []
    
    for param_file in sorted(os.listdir(PARAM_PATH)):
        run_savilerow(param_file, optimisation=opt_flag)

        with open(param_file+".info") as info_file:
            info_lines = info_file.readlines()
            solver_time = float(info_lines[0].strip().split(":")[1])
            solver_nodes = int(info_lines[6].strip().split(":")[1])

            data_time.append(solver_time)
            data_nodes.append(solver_nodes)

    return (data_time, data_nodes)




def print_data(data_time, data_nodes):
    print("Time data")
    print_data_dict(data_time)

    print("\nNode data")
    print_data_dict(data_nodes)

    #print_coefficients(data_time, data_nodes)


def print_data_dict(data_dict):
    for opt,data in data_dict.items():
        print("\n" + str(opt))
        i = 1
        for param, time in zip(get_param_list(), data):
            if i % 2 == 0:
                print("(" + str(i) + "," + str(time) + ")", end=" ")
            i += 1

        i = 1
        for param, time in zip(get_param_list(), data):
            if i % 2 != 0:
                print("(" + str(i) + "," + str(time) + ")", end=" ")
            i += 1

        print("\n --- together---")
        i = 1
        for param, time in zip(get_param_list(), data):
            print("(" + str(i) + "," + str(time) + ")", end=" ")
            i += 1



def print_coefficients(data_time, data_nodes):
    for opt in data_time.keys():
        times = data_time[opt]
        nodes = data_nodes[opt]

        i = 1
        for time,node in zip(times, nodes):
            print("(" + str(i) + "," + str(node/time) + ")", end=" ")
            i += 1

        print("\n")

def print_timenodes(data_time, data_nodes):
    for time,nodes in zip(data_time, data_nodes):
        print("(" + str(nodes) + "," + str(time) + ")", end=" ")

    print("--------")
    for time,nodes in zip(data_time, data_nodes):
        print(str(nodes) + " " + str(time))


def write_data(data_file, opt_flag="-O2", heuristic=""):
    data_time = []
    data_nodes = []
    
    for param_file in sorted(os.listdir(PARAM_PATH)):
        run_savilerow(param_file, optimisation=opt_flag)

        with open(param_file+".info") as info_file:
            info_lines = info_file.readlines()
            solver_time = float(info_lines[0].strip().split(":")[1])
            solver_nodes = int(info_lines[6].strip().split(":")[1])

            data_file.write(param_file + "," +
                            str(solver_time) + "," +
                            str(solver_nodes) + "," +
                            opt_flag + "," +
                            heuristic + "\n")
            data_file.flush()
            
            data_time.append(solver_time)
            data_nodes.append(solver_nodes)

    return (data_time, data_nodes)

