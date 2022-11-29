'''
    Tree Path Finder

    given a binary tree 
    return the branch that contains the target node 
    if no match to the target node return Null

    approach: recursion 
        when a node has no either left or right 
        then we will return none
            at the end of excuting the function call we will return none
            however, we can give it a conditional that matches the value we will return the value in a list 
            and since it triggers that recursive call
            i call just keep the recusive function call after it
        ** keep in mind that i should not be hitting the case that node.left or node.right is none
        because it will return None and values from the first branch that hits the basecase first

    approach: recursion time complexity imporved
        convert the path_finder to a helper function
        instead of adding the new value to the beginning of the list
        we can use append to add it to the end of a list which improves the time complexity to the O(1)
        and then reverse the list which is also O(n) 
        
'''


def path_finder(root, target):
    if root is None:
        return None

    if root.val == target:
        return [root.val]

    left = path_finder(root.left, target)
    if left:
        return [root.val, *left]
    right = path_finder(root.right, target)
    if right:
        return [root.val, *right]

    return None
