# Input format:
# - two space separated integers n and m
#   . n is size of array
#   . m is the number of operations
# - Each of the next m lines contain 3 space separated integers \
#   a = left index, b = right index, k = summand


def arrayManipulation(n, queries):
    list = [0 for v in range(n)]
    for i in range(len(queries)):
        for j in range(len(queries)-1):
            a = queries[i][j]
            b = queries[i][j+1]
            k = queries[i][j+2]
            for l in range(a - 1, b, 1):
                list[l] += k
    return max(list)


arr = [[1,2,100],
       [2,5,100]]

print(arrayManipulation(5, arr))