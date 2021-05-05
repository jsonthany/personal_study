class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
    def __init__(self):
      self.head = None
      
    def append(self, data):
      new_node = Node(data)
      
      if self.head == None:
        self.head = new_node
        return
      
      current = self.head
      while (current.next):
        current = current.next
        
      current.next = new_node
      
    def printList(self):
      current = self.head
      while (current):
        print(current.data)
        current = current.next
        
    def prepend(self, data):
      new_node = Node(data)
      
      new_node.next = self.head
      self.head = new_node
      
    def insertAfterNode(self, prevNode, data):
      new_node = Node(data)
      prev = self.head
      
      while (prev):
        if prev.data == prevNode:
          new_node.next = prev.next
          prev.next = new_node
          break
        
        prev = prev.next
        
    def deleteNodeKey(self, key):
      prevNode = self.head
      
      if ((prevNode) and (prevNode.data == key)):
        self.head = prevNode.next
        prevNode = None
        return
      
      currentNode = prevNode.next
      while (currentNode):
        if (currentNode.data == key):
          prevNode.next = currentNode.next
          currentNode = None
          return
          
        prevNode = prevNode.next
        currentNode = currentNode.next
        
    def deleteNodePos(self, pos):
      prevNode = self.head
      
      if (pos == 0):
        self.head = prevNode.next
        prevNode = None
        return
        
      count = 1
      currentNode = prevNode.next
      while (currentNode):
        if (count == pos):
          prevNode.next = currentNode.next
          currentNode = None
          return
        
        prevNode = prevNode.next
        currentNode = currentNode.next
        count += 1
    
    def lenIterative(self):
      count = 0
      currentNode = self.head
      
      while (currentNode):
        count += 1
        currentNode = currentNode.next
        
      return count
        
    def lenRecursive(self, node):
      
      if node == None:
        return 0
      
      return 1 + self.lenRecursive(node.next)
    
    def swapNodes(self, keyOne, keyTwo):
      
      if (keyOne == keyTwo):
        return
      
      prevOne = None
      currOne = self.head
      while ((currOne) and (currOne.data != keyOne)):
        prevOne = currOne
        currOne = currOne.next
        
      prevTwo = None
      currTwo = self.head
      while ((currTwo) and (currTwo.data != keyTwo)):
        prevTwo = currTwo
        currTwo = currTwo.next
        
      if ((not currOne) or (not currTwo)):
        return
      
      if (prevOne):
        prevOne.next = currTwo
      else:
        self.head = currTwo
        
      if (prevTwo):
        prevTwo.next = currOne
      else:
        self.head = currOne
        
      tempOne = currOne.next
      tempTwo = currTwo.next
      
      currOne.next = tempTwo
      currTwo.next = tempOne
      
    def reverseIterative(self):
      prevNode = None
      currNode = self.head
      while (currNode):
        tempNext = prevNode
        prevNode = currNode
        currNode = currNode.next
        prevNode.next = tempNext
      self.head = prevNode
      
    def reverseRecursive(self):
      
      def _reverse_Recursive(curr, prev):
        if (not curr):
          return prev
        
        tempNext = prev
        prevNode = curr
        currNode = curr.next
        prevNode.next = tempNext
        
        return _reverse_Recursive(curr = currNode, prev = prevNode)
        
      self.head = _reverse_Recursive(curr = self.head, prev = None)
      
    def mergeSorted(self, secondList):
      
      llOne = self.head
      llTwo = secondList.head
      prevNode = None
      
      while (llOne and llTwo):
        if (llOne.data <= llTwo.data):
          if (prevNode is None):
            newHead = llOne
          else:
            prevNode.next = llOne
            
          prevNode = llOne
          llOne = llOne.next
          
        else:
          if (prevNode is None):
            newHead = llTwo
          else:
            prevNode.next = llTwo
          
          prevNode = llTwo
          llTwo = llTwo.next
            
      if (not llOne):
        prevNode.next = llTwo
        
      if (not llTwo):
        prevNode.next = llOne
        
      self.head = newHead
      return self.head
    
    def removeDuplicates(self):
      
      valueSet = set()
      prev = None
      curr = self.head
      
      while (curr):
        if (curr.data not in valueSet):
          valueSet.add(curr.data)
          prev = curr
          curr = curr.next
        else:
          curr = curr.next
          prev.next = curr