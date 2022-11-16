# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def level_averages(root):
    if root is None:
        return []

    levels = []
    queue = [(root, 0)]
    while queue:
        current, level_num = queue.pop(0)

        if len(levels) == level_num:
            levels.append([current.val])
        else:
            levels[level_num].append(current.val)

        if current.left is not None:
            queue.append((current.left, level_num + 1))
        if current.right is not None:
            queue.append((current.right, level_num + 1))

    return [sum(sub)/(len(sub)) for idx, sub in enumerate(levels)]
