arr = [31, 41, 59, 26, 41, 58]
for i in range(1, len(arr)):
    key = arr[i]
    # Insert arr[i] into the sorted subarray arr[1:i - 1]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print(arr)