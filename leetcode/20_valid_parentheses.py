'''
    
    Approach: 
        use stack
        we will store the value of the map each time from the current value
        for instance if first value is '(' then we will store ')' in our stack
        is the next value is ')' in the array, then we know that we can pop the stack
        else we will keep storing the values in stack

        the issue is that what is the first element is ')' which does not exists in map keys
        then we will have a elif condition to check the stack, if the stack's length is 0 when we know that the first element does not exit in keys
        so we can return False or if the last element in the stack does not equal to the next element in the elif condition, we can also return False

'''


class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for val in s:

            if val in map.keys():
                stack.append(map[val])
            elif not stack or stack[-1] != val:
                return False
            else:
                stack.pop()

        return len(stack) == 0
