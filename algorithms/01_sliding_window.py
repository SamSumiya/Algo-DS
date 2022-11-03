'''


'''


def sliding_window_bf(arr, k):
    if len(arr) < k:
        return -1

    size = len(arr)
    max_sum = 0
    k -= 1
    i = 0

    while k < size:
        kk = k
        current_max = 0

        while kk >= i:
            current_max += arr[kk]
            kk -= 1

        max_sum = max(max_sum, current_max)

        k += 1
        i += 1

    return max_sum

def sliding_window(arr, k): 
    pass 


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
r = sliding_window_bf(arr, k)
print(r)
