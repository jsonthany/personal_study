import CustomLinkedList

ll = CustomLinkedList.LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(4)
ll.insertAfterNode(3, 10)
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