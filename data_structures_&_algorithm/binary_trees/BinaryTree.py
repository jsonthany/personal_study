class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    # choose the type of traversal type
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)
        elif traversal_type == "reverseorder":
            return self.reverse_levelorder_print(self.root)
        
        else:
            print("Traversal type " + traversal_type + " not supported")
            return False
        
    # Traversal Depth-First Approach 1
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        
        return traversal
    
    # Traversal Depth-First Approach 2
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
            
        return traversal
    
    # Traversal Depth-First Approach 3
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
            
        return traversal
    
    def levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        
        traversal = ""
        
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
    def reverse_levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        stack = Stack()
        traversal = ""
        
        while (len(queue) > 0):
            node = queue.dequeue()
            
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
                
            stack.push(node)
            
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
                
        return traversal
    
    def tree_height(self, node):
        # base case: if nothing, then return -1
        if node is None:
            return -1

        left_height = self.tree_height(node.left)
        right_height = self.tree_height(node.right)
        
        return 1 + max(left_height, right_height)
        

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Stack(object):
    def __init__(self):
        self.items = []
        
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s