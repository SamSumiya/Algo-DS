'''

589. N-ary Tree Preorder Traversal

Given a nary tree, the different from a binary tree is that the next value is not left or right but its a list of collections of nodes
So we can modify the approach for binary tree DFT approach

Approach: 
    create a stack with nary tree top in it
    use a while loop to traverse it
    the current val will be stored in output array
    then we will have to put the children list in stack but there are two small challenges
    1. we will need to use extend so it will be flattened to 1-d list
    2. we will need to get the node from the back, so we have to reverse the list
    
    we really should utilize the pop function to get the last value from the list and stack data structure to get each value to the output
    

Approach: recursion
create a empty list and a innner function

if the root has value then we will add the value to the list
thenb we will loop through the root for its children
so for a nary like 
      1
    / | \ 
   3  2  4 
 / \
5   6 

the first time we will get 1 
then we will loop throug [3, 2 ,4]
then we get 3
since 3 has 5 and 6, we will go through [5,6]
then we go down to 5
there is nothing below 5, so we will go to to 

'''

class Solution(object):
    def preorder_iter(self, root):
        if not root: return []
        stack = [root]
        out = []
        
        while len(stack):
            temp = stack.pop()
            out.append(temp.val)
            stack.extend(reversed(temp.children))
        
        return out
    
    def preorder_recur(self, root):
        def recur(root): 
            if root:
                output.append(root.val)
                for el in root.children: 
                    recur(el)

        output = [] 
        recur(root)
        return output