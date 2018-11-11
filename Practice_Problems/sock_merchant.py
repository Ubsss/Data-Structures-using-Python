# Given an array of integers, determine how many pair of intergers are in the array.
#
# For example given n = 7 in array = [1,2,1,2,1,3,2]. There is one pair of 1s and 1 pair of 2s,
# algorithm should return 2.

array = [50,10, 20, 20, 10, 10, 30, 50, 10, 20]

def find_parirs(array):
    count = 0
    dictionary = {}

    for i in array:
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] += 1

    for key in dictionary:
        count += dictionary[i] // 2

    print(dictionary)
    return count

find_parirs(array)