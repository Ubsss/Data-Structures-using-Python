array = [7,5,89,3,12,566,8]

#TC = O(n), SC = O(n)
def my_sort(arr):
    my_arr = arr[:]
    for i in range(len(arr)):
        min_numb = min(arr)
        min_idx = arr.index(min_numb)
        my_arr[i] = min_numb
        del arr[min_idx]
    return my_arr
#print(my_sort(array))


original_array = [4,5,6,7,5,3,3,5,6,7]



left = original_array[:(len(original_array)//2)]
right = original_array[(len(original_array)//2):]

print(original_array, left, right)