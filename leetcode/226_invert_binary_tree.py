'''
226. Invert Binary Tree


Intuition:
My intuition was that I will need to swap left node to right node. 
let's say 
            1
           / \ 
          2   3 
         / \  / \
        4   5 6  7 
however, if I only swap 2 and 3
the children of 2 and 3 would stay the same and it would not be correct
so we will have to swap nodes on every level. 

# Approach: 
Find the base case which is when the node is None

then we will recursively call the invert_tree function. 
we will have to swap the nodes from left to right and then pass then to the parameters

at the end of each function call, we will need to return the current root.
so the first root that has left and right is 1
then, 2 and 3 will be swapped and 
it goes down to 2 and 3 as root
then 4 and 5 will be swapped so are 6 and 7

finally, it goes down to 4 5 6 7 as they do not have left nor right
the base case if node is none will be trigger to return None
swapped nones 

and it pops the stack from the top to get the the correct inverted binary tree

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None

        root.left, root.right = root.right, root.left

        left_path = self.invertTree(root.right)
        right_path = self.invertTree(root.left)
        print(root.val)
        return root
            
a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')

a.left = b
a.right = c

so = Solution()


r = so.invertTree(a)
print(r)