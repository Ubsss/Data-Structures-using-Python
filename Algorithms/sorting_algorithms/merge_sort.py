#O(n logn)
def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        left_half = array[:mid]
        right_half = array[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i=0; j=0; k=0;
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k]=left_half[i]
                i+=1
            else:
                array[k]=right_half[j]
                j+=1
            k+=1

        while i < len(left_half):
            array[k]=left_half[i]
            i+=1
            k+=1

        while j < len(right_half):
            array[k]=right_half[j]
            j+=1
            k+=1
    return array

my_list = [54,26,93,17,77,31,44,55,20]

