'''

    Is Valid Subseqence

    approach    
        have two pointers i and j start from 0 
        
        
        loop through the array
        if array[i] == seq[j] then we will increment j by 1
        at the end if the j is the same as the len(sequence)
        then we know that j reached to the last element of seq
'''




def isValidSubsequence(array, sequence):
    i = 0
    size = len(array)
    count = 0
    j = 0
    while i < size and j < len(sequence):
        if array[i] == sequence[j]:
            count += 1
            j += 1

        i += 1
    return i == j


array = [1, 1, 1, 1, 1]
sequence = [1, 1, 1]

r = isValidSubsequence(array, sequence)
print(r)
