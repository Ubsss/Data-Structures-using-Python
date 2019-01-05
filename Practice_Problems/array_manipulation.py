def arrayManipulation(n, queries):
    # list = [0 for v in range(n)]
    # for i in range(len(queries)):
    #     if i > 0:
    #         a = queries[i][0]
    #         b = queries[i][1]
    #         k = queries[i][2]
    #
    #         for l in range(a - 1, b, 1):
    #             list[l] += k
    #
    #         print(list)
    # return max(list)

    arr = [0 for i in range(n+1)]

    for i in queries:
        arr[i[0] - 1] += i[2]
        arr[i[1]] -= i[2]

    maximum = 0
    total_sum = 0
    for i in arr:
        total_sum += i
        if total_sum > maximum:
            maximum = total_sum
    return maximum

arr = [[5,3],
       [1,5,3],
       [4,8,7],
       [6,9,1]]

print(arrayManipulation(10, arr))