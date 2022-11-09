'''
205. Isomorphic Strings


Approach: character mapping with dictionary 
    create a dictionary populate with keys from the 1st array and values from the 2nd array
    if element in t does not exits in the values and value in t does not exits in {} 
    then we can be certain that we only add uniq key value pairs to the dictionary

    then we will loop through s and t
    if element from s not in keys
    if dict[s_element] != t element 
    then return False 


'''


# def isIsomorphic(s, t):
#     my_dict = {}
#     i = 0 
#     j = 0 

#     while i < len(s): 
#         if t[i] not in my_dict.values() and s[i] not in my_dict: 
#             my_dict[s[i]] = t[i]
#         i += 1 
        

#     while j < len(s): 
#         if s[j] not in my_dict.keys(): 
#             return False
#         if my_dict[s[j]] != t[j]: 
#             return False
#         j += 1 

#     return True


class Solution:
    
    def transformString(self, s):
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        print(index_mapping)
        print(new_str)
        return " ".join(new_str)
    
    def isIsomorphic(self, s, t):
        return self.transformString(s) == self.transformString(t)

so = Solution()

s = "badc"
t = "baba"
r = so.isIsomorphic(s, t)

print(r)