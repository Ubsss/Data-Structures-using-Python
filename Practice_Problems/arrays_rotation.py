# Given an array, a, shift it's values left or right n amount of times:
#
# For example, given a = [1,2,3,4] and direction of left and n or 2, you
# should output a = [3,4,1,2].

array = [1,2,3,4,5]

def rotate_right(nums, k):

    size = len(nums)
    numsB = nums[:]

    for i in range(len(numsB)):
        if i+k >= size:
            index = (i+k)%size
        else:
            index = i+k

        nums[index] = numsB[i]

    print(nums)

def rotate_left(nums, k):
    size = len(nums)
    numsb = nums[:]

    for i in range(len(numsb)):
        if i - k <= 0:
            index = abs((i-k)%size)
        else:
            index = i - k

        nums[index] = numsb[i]

    print(nums)

rotate_left(array, 6)

