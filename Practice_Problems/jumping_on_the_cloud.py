# Given an array of clouds, clouds = [0,1,0,0,0,1,0]. 0 being safe and 1 being unsafe.
# Return the minimum numeber of jumps required to get to the last cloud while avoiding
# the unsafe clouds.
#
# For example, given c = [0,1,0,0,0,1,0]. You could jump from 0-2-4-6 providing the
# shorted number of jumps needed to reach the end.
# Making the assumptin you will never have two unsafe clouds next to each other

clouds = [0,0,1,0,0,1,0,1,0]

def minimum_number_of_jumps(array):
    jumps = 0
    i = 0

    while i < (len(array) - 1):
        if i + 2 <= len(array) - 1 and array[i + 2] == 0:
            i += 2
            jumps += 1

        elif array[i+1] == 0:
            i += 1
            jumps += 1
    return jumps


print(minimum_number_of_jumps(clouds))