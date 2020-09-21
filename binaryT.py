

class binaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_value(self):
        return self.data




# class BinaryTree:

#     def __init__(self, data):
#         self.root = binaryTreeNode(data)
        
#     def set_left_node(self, data):
#         self.root.left = binaryTreeNode(data)

#     def set_right_node(self, data):
#         self.root.right = binaryTreeNode(data)        

#     def get_left_node(self):
#         return self.root.left    

#     def get_right_node(self):
#         return self.root.right



# bin_tree = BinaryTree(1)
# bin_tree.set_left_node(2)
# bin_tree.set_right_node(3)
# root = bin_tree.get_left_node()
# root.left(4)
# root.right(5)
# root = bin_tree.get_right_node()
# root.left(6)
# root.right(7)

root = binaryTreeNode(1)
root.left = binaryTreeNode(2)
root.right = binaryTreeNode(3)
root1 = root.left
root2 = root.right
root1.left = binaryTreeNode(4)
root1.right = binaryTreeNode(5)
root2.left = binaryTreeNode(6)
root2.right = binaryTreeNode(7)

import pdb
def print_tree_preorder(r):
    # pdb.set_trace()
    if r == None:
        return
    print r.data
    print_tree(r.left)    
    print_tree(r.right)    


print_tree(root)