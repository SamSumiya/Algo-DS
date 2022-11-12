'''
102. Binary Tree Level Order Traversal

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return [] 
        stack = [ (root, 0) ]
        output = [] 

        while stack: 
            node, level = stack.pop(0)

            if level == len(output): 
                output.append([node.val])
            else: 
                output[level].append(node.val)

            if node.left: 
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        
        return output
        
        