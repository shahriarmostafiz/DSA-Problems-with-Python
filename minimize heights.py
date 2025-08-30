def minimize_height(arr,k):
    arr.sort()
    n= len(arr)
    last=arr[-1]
    first = arr[0]
    
    res= last-first
    
    for i in range(1,n):
        if arr[i]-k < 0:
            continue
        low = min(first+k, arr[i]-k)
        print("low now", low)
        high = max(last-k,arr[i-1]+k)
        print("high now", high)
        res= min(res, high-low)
        print("res now", res)
    
    return res

print(minimize_height([1,3,5,6,7],2))
        