def insertion_sort(arr):

    i = 1

    while i < len(arr):
        base = arr[i]
        j = i - 1

        while j >= 0 and base < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = base
        i += 1
    return arr


def bucket_sort(array):

    freq = [[] for i in range(10)]

    for el in array:
        key = int(el * 10)
        freq[key].append(el)

    
    for i in range(10):
        freq[i] = insertion_sort(freq[i])
    
    k = 0 

    for i in range(10): 
        for j in range(len(freq[i])): 
            array[k] = freq[i][j]
            k += 1 
    
    return array








array = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434]

r = bucket_sort(array)

print(r)