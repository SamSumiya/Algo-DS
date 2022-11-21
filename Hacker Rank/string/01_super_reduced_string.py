'''
superReducedString 

We will need to keep trimming the string if the two adjacent elements are the same.
So we will need to always go back to the first elements and check what is the next element right to its right side
Since there are cases like 'aba' the string will never change, we will need to have an addtional condition to track the progress 

Ituition: 
We need to have a boolean to check if the changed is true or false, basically if two adjancent elements are equal to each other.
we will changed the boolean to true.

we will just need to loop through the string and remove the strings that meets s[i] == s[i+1] condition
if it does, we can break out from the loop, we also changed the condition back to true so the outer loop will be true again.



'''

class Solution:
    def superReducedString_1(self, s):
        changed = True
        output = 'Empty String'
        i = 0

        while changed and s != "":
            changed = False
            for i in range(len(s) - 1):
                if s[i] == s[i+1]:

                    changed = True
                    s = s[:(i)] + s[(i+2):]
                    break

        return output if len(s) == 0 else s
    
    def superReducedString_2(self, s):
        changed = True
        output = 'Empty String'

        while changed and s != "":
            changed = False
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    changed = True
                    s = s[:(i)] + s[(i+2):]
                    break
                i += 1
        return output if len(s) == 0 else s



ss = 'abaa'
so = Solution()

r_1 = so.superReducedString_1(ss)
r_2 = so.superReducedString_2(ss)
print(r_1, r_2)