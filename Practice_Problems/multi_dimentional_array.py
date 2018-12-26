# list = [[0 for i in range(10)] for j in range(10)]

# arr = [1,1,1, 0, 1]
#
# def jumps(array):
#     count = 0
#     jumps = 0
#
#     for i in range(0, len(array)):
#         if(array[i] == 1):
#             count = 0
#         else:
#             count += 1
#             jumps = max(jumps, count)
#     return jumps+1
#
#
# print(jumps(arr))

# arr = ["N"]
#
# def attendance(array, m):
#     streak = 0
#     count = 0
#
#     for i in array:
#         for j in i:
#             if j == 'Y':
#                 streak += 1
#             else:
#                 streak = 0
#
#         if streak == len(j) - 1:
#             count += 1
#
#     return count
#
# print(attendance(arr, 2))

