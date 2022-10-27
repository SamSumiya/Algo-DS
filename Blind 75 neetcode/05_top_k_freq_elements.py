'''
    Top K Frequent Elements

    Given a list and target number
    we should reture the top target most frequent numbers

    https://leetcode.com/problems/top-k-frequent-elements/

    approach: bucket sort 

        create a hashmap so we can store the element and how many times we have seen the elements 
        and then create a nested list with length + 1 of sub list

        populate the hashmap with get(el, 0)
        count[n] = 1 + count.get(el, 0) which means if count has n then increment the value by 1 else create a new key with el and value as 0 initally and increment it to 1

        then we can use the value from count as index for the right list to store the key which is the element in the original list

        at this point, we should have each element in the right nested lists

        so we will need to extract the values in the right order. 

        we can reverse the list 
            lets say if there are 2 5s and 3 2s
                the list will look like [[], [], [5], [3], [], [], []]
            so when we reverse the list
                it will look like 
                [[], [], [3], [5], [], [], []]
            which is the right order of frequencies
            we will just need to place there two values in an additional list 
            we will need to access the nested list by using the length of the list
            so we can go to each nested list and get the values
        then return the final list with the values
'''


from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {} 
    freq = [[] for i in range(len(nums) + 1)]
        
    for n in nums: 
        count[n] = 1 + count.get(n, 0)
        
    for key, val in count.items(): 
        freq[val].append(key)
        
    output = []
    reversed_freq = freq[::-1]
    for i in range(len(reversed_freq)): 
        
        for el in reversed_freq[::-1][i]:    
            output.append(el)
            
            if len(output) == k: 
                return output


nums = [1,1,1,2,2,3]
k = 2
r = topKFrequent(nums, k)

