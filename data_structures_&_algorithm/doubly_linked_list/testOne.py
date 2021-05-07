import DoublyLinkedList

dll = DoublyLinkedList.DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.prepend(0)
dll.printList()

print("")
dll.addNodeAfter(2,102)
dll.addNodeBefore(102,101)
dll.printList()

print("")
dll.addNodeAfter(0,100)
dll.addNodeAfter(4,"final")
dll.addNodeBefore(0,-1)
dll.printList()

print("")
dll.deleteNode(-1)
dll.printList()

print("")
dll.reverse()
dll.printList()