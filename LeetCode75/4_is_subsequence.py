'''
392. Is Subsequence

Approach 1:
    Since t is longer than s
    we can set two variables i and j to 0 
    we will loop through t and only increment i when the values match

    then at the end we can check if i equals to the length of s
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0 

        while j < len(t) and i < len(s): 
            if t[j] == s[i]: 
                i += 1
        
            j += 1 
        return i == len(s)

    def isSub_recur(self, s, t): 
        def helper(s_l, t_l):
            if s_l == L: return True
            tmp = t.find(s[s_l], t_l)
            if tmp == -1: return False
            return helper(s_l + 1, t_l + 1)
        L = len(s)
        return helper(0,0)
