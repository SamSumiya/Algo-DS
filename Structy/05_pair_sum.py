'''

    Pair Sum

    given a list of numbers and pair of 2 euqals to the target is guaranteed.
    return the indices of the two numbers 
    * if the element are the same, the indices must be diffirent 
    [1,1] = 2
    return 0 and 1

    approach: brute force - nested loop
    
    1. loop the list from index, so we will get the first element
    2. loop the list from the index + 1, so we will get the all elements in the list except the first one
    3. find a pair that equals to the target number
    4. if not, keep the process till the last element
    5. return the indices
'''

def pair_sum_bf(numbers, target_sum): 
    i = 0
    size = len(numbers)

    while i < size:
        j = i + 1
        n_1 = numbers[i]

        while j < size:
            n_2 = numbers[j]

            if n_1 + n_2 == target_sum:
                return(i, j)
        i += 1



def pair_sum(numbers, target):
    dict = {}

    for idx, el in enumerate(numbers):
        diff = target - el
        if diff in dict:
            return (idx, dict[diff])

        dict[el] = idx
