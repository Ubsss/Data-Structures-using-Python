# Given an array, a, shift it's values left or right n amount of times:
#
# For example, given a = [1,2,3,4] and direction of left and n or 2, you
# should output a = [3,4,1,2].

array = [1,2,3,4,5]

def rotate_right(nums, k):
    my_nums = nums[:]
    lens = len(nums)

    for i in range(lens):
        if (i + k) >= lens:
            pos = (i + k) % lens
            my_nums[pos] = nums[i]
            print(pos)
        if (i + k) < lens:
            pos = (i + k)
            my_nums[pos] = nums[i]
    return my_nums

print(rotate_right(array,26))

# def rotate_left(nums, k):
#     size = len(nums)
#     numsb = nums[:]
#
#     for i in range(len(numsb)):
#         if i - k <= 0:
#             index = abs((i-k)%size)
#         else:
#             index = i - k
#
#         nums[index] = numsb[i]
#
#     print(nums)
#
# rotate_left(array, 6)

