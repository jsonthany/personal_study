import CustomLinkedList

ll = CustomLinkedList.LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(4)
ll.prepend(4)
ll.append(4)
ll.append(4)
ll.append(2)
ll.insertAfterNode(3,10)
ll.deleteNodeKey(10)
ll.deleteNodePos(10)
ll.swapNodes(4,2)

ll.printList()
print("")

ll.reverseIterative()
ll.printList()
print("")

ll.reverseRecursive()
ll.printList()
print("")

print(ll.lenIterative())
print(ll.lenRecursive(ll.head))

print("")
print(ll.getNthToLastNodeOne(3))
print(ll.getNthToLastNodeTwo(3))

print("")
print(ll.countDataIterative(4))
print(ll.countDataRecursive(ll.head,4))
print(ll.countDataIterative(2))
print(ll.countDataRecursive(ll.head,2))

print("")
ll.rotate(2)
ll.printList()