'''

    Five Sort 

    given a list of numbers that contains some 5s 
    we need to swap the position of 5 to the end of the list excluding 5 itself
    if the five is alway at the end 

    [12, 5, 1, 5, 12, 7] =>  [12, 7, 1, 12, 5, 5] 
    [5, 2, 5, 6, 5, 1, 10, 2, 5, 5] => [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 


    Approach: nested loops
    1. create pointer1 which equals to 0 
    2. create pointer2 which equals to last index of the list
    3. loop through the list 
    4. we will start from pointer1 and if it is 5
        a. we will need to check if the current last element is 5 or not
        b. if it is 5, we will need to subtract 1 from it
        c. else we can swap the elements
    6. continue the process until pointer1 meets pointer2 
    7. return the modified list

    Approach: two pointer
    similar with the one above 
    but instead of using a nested loop
    1. we can just simply check if the pointer2 is 5 or not
    2. check if pointer 1 is 5 or not
        a. if it is we can swap the elements 
        b. increment pointer1 by one
    3. if none of the requirements meet
        a. we will just increment pointer1 by 1

'''


def five_sort_bf(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] == 5:
            while nums[j] == 5:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i += 1

    return nums


def five_sort(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return nums
