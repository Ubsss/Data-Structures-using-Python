def grading_students(my_arr):
    arr = my_arr[1:]
    for i in range(len(arr)):
        grade = ((arr[i]//5) + 1)*5
        if ((grade - arr[i])<3) and grade >= 38:
            arr[i] = grade
    return arr

list = [4,73,67,38,33]

print(grading_students(list))