'''

    Is Palindrome
    https://leetcode.com/problems/valid-palindrome/submissions/

    Approach: two pointers
    

'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = s.lower()
        i = 0 
        j = len(s) - 1
        alphabets = 'abcdefghijklmnopqrstuvwxyz0123456789'
        

        while i < j:
            while i < j and lower_str[i] not in alphabets: 
                i += 1
            while i < j and lower_str[j] not in alphabets: 
                j -= 1 
            if lower_str[i] != lower_str[j]: 
                return False
            i += 1
            j -= 1 
        return True