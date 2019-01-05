array = [7,1,3,2,4,5,6]

# def minimum_swaps(arr):
#     min = 0
#     for i in range(len(arr)):
#         if arr[i] != i + 1:
#             for j in range(i,len(arr)):
#                 if arr[j] == i + 1:
#                     temp = arr[i]
#                     arr[i] = arr[j]
#                     arr[j] = temp
#                     min += 1
#     return min
#
# print(minimum_swaps(array))


def minSwaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    ans = 0

    for i in range(n):

        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i

        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans

print(minSwaps(array))
