# Given a 6 by 6 2D array, find the largest sum of an hourglass in the array

list = [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]

def hour_glass(arr):
    # float('inf') - largest possible number in python
    # float('-inf') - smallest possible number in python

    my_list = []

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            count = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                     arr[i+1][j+1] + \
                     arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            my_list.append(count)
    return max(my_list)

print(hour_glass(list))