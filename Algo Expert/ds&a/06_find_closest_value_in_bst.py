'''
    Find the closest value in BST


    Approach: Breadth First Traverse
        use queue technique to traverse the tree
        set a difference to positive infinity
        update the different if target - current.val is less 
        if it is less then we know the current val is closer to the target and we will also update the closest value
        return closest value at the end



'''

from collections import deque

def findClosestValueInBst(tree, target):
    closest_val = 0
    distance = float('inf')
    queue = deque([tree])

    while queue:
        current = queue.popleft()
        diff = abs(current.value - target)

        if diff < distance:
            distance = diff
            closest_val = current.value
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return closest_val


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
