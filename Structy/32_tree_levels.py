

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_levels(root):
    if root is None:
        return []

    stack = [(root, 0)]
    levels = []

    while stack:
        node, level = stack.pop(0)
        if len(levels) == level:
            levels.append([node.val])
        else:
            levels[level].append(node.val)

        if node.left:
            stack.append((node.left, level + 1))
        if node.right:
            stack.append((node.right, level + 1))

    return levels


'''
if root is None: return []

stack = [root]
output = [] 

while stack: 
    curr = stack.pop(0)
    print(curr.val)
    curr_pair = [curr.val, level]
    v, l = curr_pair
    
    # output.append([])  
    print(l)
    output.append([v])
    
    if curr.left:
      stack.append(curr.left)
    if curr.right:
      # level += 1 
      stack.append(curr.right)
    
  return output
'''
