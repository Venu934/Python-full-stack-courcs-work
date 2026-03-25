def insert_into_sorted(arr, x):
    arr.append(0)              # add space
    i = len(arr) - 2           # last valid element index
    
    while i >= 0 and arr[i] > x:
        arr[i + 1] = arr[i]    # shift right
        i -= 1
    
    arr[i + 1] = x             # insert element
    return arr


arr = [1, 3, 5, 7]
x = 4

print(insert_into_sorted(arr, x))
