import os
import subprocess
import math
from gathering import *


times, nodes = get_data()

i = 1
for param, time, node in zip(get_param_list(), times, nodes):
    if i % 2 == 0:
        print("(" + str(i) + "," + str(node) + ")", end=" ")
    i += 1


i = 1
for param, time, node in zip(get_param_list(), times, nodes):
    if i % 2 != 0:
        print("(" + str(i) + "," + str(node) + ")", end=" ")
    i += 1

