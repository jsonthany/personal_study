import CircularLinkedList

cll = CircularLinkedList.CircularLinkedList()
cll.append(1)
cll.append(3)
cll.append(8)
cll.append(7)
cll.prepend(100)
cll.printList()

print("")
cll.removeNode(7)
cll.printList()

print("")
print(cll.__len__())