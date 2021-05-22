class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, new_value):
        self.insert_helper(self.root, new_value)
        
    def insert_helper(self, curr_node, new_value):
        if new_value <= curr_node.data:
            if curr_node.left:
                self.insert_helper(curr_node.left, new_value)
            else:
                curr_node.left = Node(new_value)
        else:
            if curr_node.right:
                self.insert_helper(curr_node.right, new_value)
            else:
                curr_node.right = Node(new_value)
                
    def search(self, find_val):
        return self.search_helper(self.root, find_val)
        
    def search_helper(self, curr_node, find_val):
        if curr_node:
            if curr_node.data == find_val:
                return True
            elif find_val <= curr_node.data:
                return self.search_helper(curr_node.left, find_val)
            else:
                return self.search_helper(curr_node.right, find_val)
        else:
            return False
        
    def is_bst_satisfied(self):
        return self.is_bst_satisfied_helper_one(self.root)
        # return self.is_bst_satisfied_helper_two(self.root)

    def is_bst_satisfied_helper_one(self, curr_node):
        if curr_node:
            if curr_node.left:
                if curr_node.data >= curr_node.left.data:
                    self.is_bst_satisfied_helper(curr_node.left)
                else:
                    return False
            if curr_node.right:
                if curr_node.data <= curr_node.right.data:
                    self.is_bst_satisfied_helper(curr_node.right)
                else:
                    return False

        return True

    def is_bst_satisfied_helper_two(self, curr_node):
        if not curr_node:
            return True
        
        if curr_node.left:
            if curr_node.data < curr_node.left.data:
                return False
            
        if curr_node.right:
            if curr_node.data > curr_node.right.data:
                return False
            
        if not self.is_bst_satisfied_helper_two(curr_node.left):
            return False
        if not self.is_bst_satisfied_helper_two(curr_node.right):
            return False
        
        return True
