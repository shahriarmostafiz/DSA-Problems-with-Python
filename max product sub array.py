def max_product_sub_array(arr):
    max_prod = arr[0]
    curr_min= arr[0]
    curr_max= arr[0]
    
    for i in range (1,len(arr)):
        
        temp = max(arr[i],curr_min*arr[i], curr_max*arr[i])
        curr_min= min (arr[i],curr_min*arr[i], curr_max*arr[i])
        curr_max=temp
        max_prod= max(curr_max,max_prod)
    return max_prod
result = print(max_product_sub_array([-2,1,3,-4,6]))
        