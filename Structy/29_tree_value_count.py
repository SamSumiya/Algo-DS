'''
    Tree Value Count 


    given a binary tree and a target
    return a count if the value equals to the target

    approach: recursion 
        base case return count which is 0 
        if node.val == target
            count += 1
        and recursively call left and right
        at the end of each function call 
        we will return count + left and right
    
    approach: recursion 2
        modification is when there is match we will return 1 else return 0
        and assign a variable such as match to it
        then we will just need to increment match and return it at the end
'''


def tree_value_count_recur(root, target, count=0):
    if root is None:
        return count

    if root.val == target:
        count += 1
    left = tree_value_count_recur(root.left, target)
    right = tree_value_count_recur(root.right, target)

    return count + left + right


def tree_value_count_recur_2(root, target):
  if root is None: return 0 

  match = 1 if root.val == target else 0 
  
  left = tree_value_count_recur_2(root.left, target)
  right = tree_value_count_recur_2(root.right, target)
  
  return match + left + right