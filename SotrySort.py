import time

def sotry_sort(arr=list):
    # Base case when lenght of the list is less than or equal to 2
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[::-1]
        return arr
    elif len(arr) < 2:
        return arr

    # Divides the list into pairs, assigning in a dictionary the low value as the key, and the high one as the value
    high_low = {}
    for i in range(0, len(arr), 2):
        if i+1 == len(arr):
            high_low[arr[i]] = None
        else:
            a = arr[i]
            b = arr[i+1]
            if a > b:
                high_low[b] = a
            else:
                high_low[a] = b

    # Recursion call of the lowest values
    low_vals = sotry_sort(list(high_low.keys()))
    sort = low_vals.copy()

    # Insertion method for the bigger values with binary search
    for key in low_vals:
        val = high_low[key]

        if val is None:
            continue

        high = len(sort)
        low = 0
        mid = (high + low)//2

        while low < high:
            if(sort[mid] < val):
                low = mid + 1
            elif(sort[mid] > val):
                high = mid
            mid = (high + low)//2

        sort.insert(mid, val)
    return sort

# Real time test
start = time.perf_counter()

sotry_sort([42, -7, 13, 0, 89, -34, 5, 76, -1, 28,
 64, -92, 11, 37, -56, 90, 3, -18, 71, 24,
 -63, 8, 55, -4, 19, 100, -81, 6, 31, -27,
 47, -9, 2, 68, -45, 14, 83, -60, 26, 1,
 -99, 58, 35, -12, 72, 9, -70, 21, 40, -2]) # Example with 50-integers long input

end = time.perf_counter()

print(f"Elapsed time: {end - start:.6f} seconds")
