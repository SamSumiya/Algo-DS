'''
    All Tree Paths

    given a binary tree 
    return a 2-d array contains all the paths from the root node the each leaft node


    approach: recursion
        when node is none rethrn [] 
        when node has node left and right node return the value from that node and nested in a 2-d array
        each function excution, we will move up one level in the tree so we can add the new value to the 2-d array
        the way to add it 
            we will have a branh from the leaf node but left or right might have more than just one list
            so we should loop the left or right side
            and simply add the root.val to the beginnin
        then we should create a empty list and concat the result to this new list


'''


def all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    all_paths = []

    left_sub_path = all_tree_paths(root.left)
    for left in left_sub_path:
        all_paths.append([root.val, *left])
    right_sub_path = all_tree_paths(root.right)
    for right in right_sub_path:
        all_paths.append([root.val, *right])

    return all_paths
