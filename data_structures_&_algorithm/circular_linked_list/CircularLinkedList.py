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
            
    def removeNodeKey(self, key):
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
        length = self.__len__()
        midpoint = length // 2
        count = 0
        
        if (length == 0):
            return None
        if (length == 1):
            return self.head
        
        prev = None
        curr = self.head
        
        newLinkedList = CircularLinkedList()
        
        while (midpoint > 0):
            prev = curr
            curr = curr.next
            midpoint -= 1
        prev.next = self.head
        
        while (curr.next != self.head):
            newLinkedList.append(curr.data)
            curr = curr.next
        newLinkedList.append(curr.data)
        
        self.printList()
        print("")
        newLinkedList.printList()
        
    def removeNodeNode(self, node):
        if (self.head):
            if (self.head == node):
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
                    if (curr == node):
                        prev.next = curr.next
                        curr = None
                        break
                    
    def josephusCircle(self, step):
        count = step
        curr = self.head
        
        while (self.__len__() > 1):
            while (count > 1):
                curr = curr.next
                count -= 1
            self.removeNodeNode(curr)
            curr = curr.next
            count = step