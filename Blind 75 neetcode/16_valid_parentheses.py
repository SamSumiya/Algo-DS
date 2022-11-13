'''
20. Valid Parentheses

'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_map = {
            '(':')',
            '[':']',
            '{':'}',
        }

        stack = [] 

        for val in s: 
            if val in parentheses_map.keys(): 
                stack.append(parentheses_map[val])
            elif len(stack) == 0 or stack[-1] != val: 
                return False
            elif stack[-1] == val:
                stack.pop()
        
        return len(stack) == 0
