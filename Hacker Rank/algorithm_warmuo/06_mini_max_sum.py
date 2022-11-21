def miniMaxSum(arr):
    total_sum = sum(arr)
    max_n = max(arr)
    min_n = min(arr)
    print(total_sum - max_n, total_sum - min_n) 
