# Given an array of integers, determine how many pair of integers are in the array.
#
# For example given n = 7 in array = [1,2,1,2,1,3,2]. There is one pair of 1s and 1 pair of 2s,
# algorithm should return 2.

array = [50,10, 20, 20, 10, 10, 30, 50, 10, 20]

def min_pairs(list):
    pairs = 0
    dictionary = {}

    for i in range(len(list)):
        if list[i] not in dictionary:
            dictionary[list[i]] = 0
        dictionary[list[i]] += 1

    for i in dictionary.values():
        pairs += i//2

    return pairs

print(min_pairs(array))