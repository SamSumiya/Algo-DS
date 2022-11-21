def diagonalDifference(arr):
    left_diagnoal_sum = 0
    right_diagnoal_sum = 0
    i = j = 0 
    
    while i < len(arr): 
        while j <= i:
                left_diagnoal_sum += arr[i][i]
                right_diagnoal_sum += arr[i][len(arr) - 1 - i]
                j += 1 
        i += 1
    return abs(left_diagnoal_sum - right_diagnoal_sum)