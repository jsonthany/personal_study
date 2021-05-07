# link: https://www.educative.io/courses/ds-and-algorithms-in-python/

class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        newNode = Node(data)
        if (not self.head):
            self.head = newNode
            newNode.next = newNode
        else:
            curr = self.head
            while (curr.next != self.head):
                curr = curr.next
            curr.next = newNode
            newNode.next = self.head
    
    def prepend(self, data):
        newNode = Node(data)
        curr = self.head
        newNode.next = self.head
        
        if (not self.head):
            newNode.next = newNode
        else:
            while (curr.next != self.head):
                curr = curr.next
            curr.next = newNode
            
        self.head = newNode
    
    def printList(self):
        curr = self.head
        
        while (curr):
            print(curr.data)
            curr = curr.next
            if (curr == self.head):
                break
            
    def removeNode(self, key):
        if (self.head):
            if (self.head.data == key):
                curr = self.head
                if (curr.next == self.head):
                    self.head = None
                else:
                    while (curr.next != self.head):
                        curr = curr.next
                    curr.next = self.head.next
                    self.head = self.head.next
            else:
                prev = None
                curr = self.head
                while (curr.next != self.head):
                    prev = curr
                    curr = curr.next
                    if (curr.data == key):
                        prev.next = curr.next
                        curr = None
                        break
                    
    def __len__(self):
        count = 0
        curr = self.head
        while (curr):
            count += 1
            curr = curr.next
            if (curr == self.head):
                break
        return count
    
    def splitList(self):
        pass