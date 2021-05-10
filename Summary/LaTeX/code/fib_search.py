def fibSearch(arr, data):
    max = len(arr) - 1
    y = getY(fib, max + 1) # Find the largest index, which its value is smaller than data.
    m = max - fib[y] 
    x = y - 1
    i = x
    if arr[i] < data: # Check at first.
        i += m
    while fib[x] > 0:
        if arr[i] < data:
            x -= 1
            i += fib[x]
        elif arr[i] > data:
            x -= 1
            i -= fib[x]
        else:
            return i
    return -1