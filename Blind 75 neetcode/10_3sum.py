'''
    3 Sum


    approach:
        This is a pretty cool question that has several nuances that I had to understand
        
        1. if I have a while loop and use the keyword continue to skip some certain indexes
            we will need to increment the index from the getgo so we will skip the first index which is not ideal we will miss the first value
            by using the keyword, we can successfully move on to the next index without do anything about it
        2. moving the index
            lets say we have a left value with the rest of value that will sum to 0 
            we just need to move one index to the next one so the while loop will go on
            however, if the next value is the same as the previous one, we can use another while loop to skip the next value
            until it has a value that is different from the one that we were on previously
        
        [[How to optimize it??]]
        3. if the current value is greater than 0
            we know that left or right will also be greater 0 
            what we know is that there will have no sum that is going to be 0
            we can break the loop there 
        4. since there will also be 2 numbers after the current num 
            we only need get to current index up to the length - 1 - 2

            
        iterate through the list with for loop
        use the sorted two sum approach for left index and right index
        left index needs + 1
        right index(length of the list) - 1
        then check if the total current_value + list(left) + list(right) is 0 or not 
        if it is we can push the values into output list
            and increment left to the next index
                however, we will also need to keep checking if the element after equals to it or not
                    if it does, we will just keep incrementing the left index
        if total is less than the 0
            we should increment left index
        if total is great than 0
            we should decrement right index
        



'''



from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    output = [] 
    sorted_nums = sorted(nums)
        
        
    for i, n in enumerate(sorted_nums[:-2]): 
        if n > 0: 
            break
        if i > 0 and n == sorted_nums[i-1]: 
            continue
        print(i, 'this is iii')
        j = i + 1
        k = len(nums) -1 
            
        while j < k:
            t = n + sorted_nums[j] + sorted_nums[k]

            if t > 0: 
                k -= 1
            elif t < 0: 
                j += 1
            else: 
                output.append([n , sorted_nums[j] , sorted_nums[k]])
                j += 1
                while sorted_nums[j] == sorted_nums[j-1] and j < k: 
                    j += 1
    
    return output


nums = [-2,0,1,1,2]
r = threeSum(nums)
print(r)

'''
Wrong approach!!!
def threeSum(nums: List[int]) -> List[List[int]]:
        if set(nums) == {0} : return [[0,0,0]]
        i = 0
        j = i + 1
        k = len(nums) - 1
        sorted_nums = sorted(nums)
        output = [] 
        uniq_output = set([])
        op = [] 
        while i < k: 
            
            total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
            
            if total == 0: 
                output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                i += 1
            if sorted_nums[k] - sorted_nums[i] - sorted_nums[j] != 0: 
                k -= 1 
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0: 
                    output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                k += 1
            if sorted_nums[j] - sorted_nums[i] - sorted_nums[k] > 0: 
                # print(sorted_nums[j], sorted_nums[i], sorted_nums[k])
                j -= 1
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0: 
                    output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
            if sorted_nums[j] - sorted_nums[i] - sorted_nums[k] < 0:
                print(sorted_nums[j], sorted_nums[i], sorted_nums[k])
                j += 1
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0: 
                    output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
            if sorted_nums[i] - sorted_nums[j] - sorted_nums[k] != 0: 
                i += 1
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0: 
                    output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
            
                
            # i = 1

        print(output)
        
        for el in output:
            
            if tuple(el) not in uniq_output and el != [0,0,0]: 
                uniq_output.add(tuple(el))
        
        for el in uniq_output: 
            op.append(list(el))
        
        
        return op
'''

    


