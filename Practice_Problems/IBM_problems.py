# def  mergeStrings(a, b):
#     new_string = ""
#     i = 0
#     j = 0
#
#     while i<len(a) and j<len(b):
#         new_string += a[i]
#         new_string += b[i]
#         i+=1
#         j+=1
#     if i != len(a):
#         for g in range(i, len(a), 1):
#             new_string += a[g]
#     if j != len(b):
#         for k in range(j,len(b), 1):
#             new_string += b[k]
#     return new_string
#
# print(mergeStrings("helloks", "worldghhhh"))

# def maxDifference(a):
#     count = a[1] - a[0]
#     min = a[0]
#
#     for i in range(1, len(a)):
#         if(a[i]-min >count):
#             count = a[i] - min
#
#         if(a[i] < min):
#             min = a[i]
#
#     return count
#
# print(maxDifference(array))

array = [7, 1, 3, 2, 4, 5, 6]


def min_swaps(arr):

    swaps = 0

    for i in range (len(arr)):
        for j in range(i, 0, -1):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swaps += 1

    return swaps

print(min_swaps(array))