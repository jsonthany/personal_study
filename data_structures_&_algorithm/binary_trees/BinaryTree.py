class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        
    # Traversal Depth-First Approach
    
    