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