'''
    Group Anagram
    https://leetcode.com/problems/group-anagrams/submissions/

    Subset of Arrays and Hashing

    given a list that contains words and some of them are potential anagrams
    the job is to group the same anagrams into the same list and return a 2-d list


    approach: hashmap

        create a new hashmap
        sorted each element in the list and use it as the key and store the unsorted element as values
        then we will check it the sorted element exists as key, if it does,
        append the value to the value list

        at the end, we can extract the values out from the hashmap
        and push each list into a new list

        return the output at the end
'''


from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []

        for el in strs:
            sorted_el = sorted(el)
            sorted_el = ''.join(sorted_el)
            if sorted_el not in hashmap:
                # sorted_el = ''.join(sorted_el)
                hashmap[sorted_el] = [el]
            else:
                if sorted_el in hashmap:
                    hashmap[sorted_el].append(el)

        for _, value in hashmap.items():
            output.append(value)

        return output

    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            count = [1] * 26

            for el in word:
                count[ord(el) - ord('a')] += 1
            hashmap[tuple(count)].append(word)

        return hashmap.values()

    def groupAnagrams_3(self, strs):
        groups = {}

        for word in strs:
            alphabets = [0 for _ in range(26)] 
            
            for letter in word:
                idx = ord(letter) - ord('a')
                alphabets[idx] += 1  
                
            if tuple(alphabets) not in groups: 
                groups[tuple(alphabets)] = [word]
            else:
                groups[tuple(alphabets)].append(word)

        return groups.values()