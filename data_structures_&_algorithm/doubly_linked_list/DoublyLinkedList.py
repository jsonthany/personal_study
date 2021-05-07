class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        
        newNode = Node(data)
        
        if (self.head == None):
            self.head = newNode
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = newNode
            newNode.prev = curr
            
    def prepend(self, data):
        
        newNode = Node(data)
        
        if (self.head == None):
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            
    def printList(self):
        curr = self.head
        while (curr):
            print(curr.data)
            curr = curr.next
            
    def addNodeAfter(self, key, data):
        curr = self.head
        while (curr):
            if (curr.data == key):
                newNode = Node(data)
                if (curr.next):
                    newNode.next = curr.next
                    curr.next.prev = newNode
                newNode.prev = curr
                curr.next = newNode
                break
            curr = curr.next
    
    def addNodeBefore(self, key, data):
        curr = self.head
        
        if (self.head.data == key):
            self.prepend(data)
            return
        
        curr = curr.next
        
        while (curr):
            if (curr.data == key):
                newNode = Node(data)
                prev = curr.prev
                prev.next = newNode
                newNode.prev = prev
                newNode.next = curr
                curr.prev = newNode
                return
            curr = curr.next
    
    def deleteNode(self, key):
        
        curr = self.head
        
        while (curr):
            if ((curr.data == key) and (curr == self.head)):
                # case 1
                if (curr.next == None):
                    curr = None
                    self.head = None
                    return
                # case 2
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return
            else:
                if (curr.data == key):
                    # case 3
                    if (curr.next):
                        nxt = curr.next
                        prev = curr.prev
                        prev.next = nxt
                        nxt.prev = prev
                        
                        curr.next = None
                        curr.prev = None
                        curr = None
                        return
                    # case 4
                    else:
                        prev = curr.prev
                        prev.next = None
                        
                        curr.prev = None
                        curr = None
                        return
                    
            curr = curr.next

    
    def reverse(self):
        
        temp = None
        curr = self.head
        
        while (curr):
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        # in case only has one node
        if (temp):
            self.head = temp.prev