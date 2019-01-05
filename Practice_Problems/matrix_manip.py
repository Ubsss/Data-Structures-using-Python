matrix = [['*','','',''],
          ['','','*',''],
          ['','','',''],
          ['','','','*']]

def most_occurance(arr):
    my_matrix = arr[:]
    list = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == '*':
                list.append(i), list.append(j)

    for i in range(len(my_matrix)):
        for j in range(len(my_matrix)):
            dist_1 = (abs(list[0] - i) + abs(list[1] - j))
            dist_2 = (abs(list[2] - i) + abs(list[3] - j))
            dist_3 = (abs(list[4] - i) + abs(list[5] - j))
            my_matrix[i][j] = min(dist_1,dist_2,dist_3)

    return my_matrix

print(most_occurance(matrix))