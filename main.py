import numpy
import math
import matplotlib.pyplot as plt
import numpy as np


def compute1RM(weight, reps):
    if reps == 1:
        return weight
    return weight * (1 + 1 * reps / 30)


def computeXRM(one_rm, reps=None, weight=None):
    if reps == 1:
        return one_rm
    if weight:
        return (one_rm - weight) / weight * 30.
    elif reps:
        return one_rm / (1 + 1 * reps / 30.)
    else:
        raise AttributeError("select reps or weight")


weight = 90
reps = 5
reps_min = 4
reps_max = 12
weight_incr = 2.5
weight_range_down = 20
weight_range_up = 20

print(f"{weight}x{reps} :")
one_rm = compute1RM(weight, reps)
print(f"{weight}x{reps} : {one_rm}")
one_rm_incr = 1
one_rm_goal = one_rm+one_rm_incr

for test_weight in numpy.arange(weight - weight_range_down, weight + weight_range_up + weight_incr, weight_incr):
    if test_weight > one_rm_goal:
        break
    float_rep = computeXRM(one_rm_goal, weight=test_weight)
    int_rep = math.ceil(float_rep)
    one_rm_candidate = compute1RM(test_weight, int_rep)
    print(f"{int_rep}\tx{test_weight}kg : {compute1RM(test_weight, int_rep)}kg")
    plt.plot([int_rep, 1],[test_weight, one_rm_candidate])

plt.xticks(np.arange(1, reps_max, 1))
plt.xlim(1, reps_max)
plt.yticks(np.arange(weight - weight_range_down, weight + weight_range_up, 2.5))
plt.ylim(weight - weight_range_down, weight + weight_range_up)
plt.grid(axis='both')
plt.show()