# given an array => [0,3,2,6,0,-1]
# return the largest concurrent multiple => 36

list = [0,3,2,6,0,-1]

def largest_multiple(arr):
    if len(arr) < 2:
        return "error"
    largest_mul = float("-inf")
    for i in range(len(arr)-1):
        local_mult = 1
        for j in range(i, len(arr)):
            local_mult *= arr[j]
            if local_mult > largest_mul:
                largest_mul = local_mult
    return largest_mul

print(largest_multiple(list))

