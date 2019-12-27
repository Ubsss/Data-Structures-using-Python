matrix = [['*','','',''],
          ['','','*',''],
          ['','','',''],
          ['','','','*']]

my_matrix = matrix[:]
my_stars = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == '*':
            my_stars.append((i, j))

local_min = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        for x in my_stars:
            local_min_local = (((i-x[0])**2 + (j-x[1])**2))**0.5

            if local_min_local < local_min:
                local_min = local_min_local

            my_matrix[i][j] = local_min

print(my_matrix)