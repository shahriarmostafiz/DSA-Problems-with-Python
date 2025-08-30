def max_sub_array_sum(arr):
    res = arr[0]
    max_sum= arr[0]
    for i in range(1,len(arr)):
        max_sum= max((max_sum +arr[i]), arr[i])
        res = max(max_sum,res)
    return res

result = max_sub_array_sum([1,2,4,-6,-4,5,6])
print("result",result)
        