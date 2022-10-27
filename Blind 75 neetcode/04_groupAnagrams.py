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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

        for key, value in hashmap.items():
            output.append(value)

        return output
