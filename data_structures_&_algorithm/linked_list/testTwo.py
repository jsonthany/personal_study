import CustomLinkedList

llOne = CustomLinkedList.LinkedList()
llOne.append(1)
llOne.append(3)
llOne.append(8)
llOne.append(10)
llOne.append(12)
llOne.printList()

print("")

llTwo = CustomLinkedList.LinkedList()
llTwo.append(1)
llTwo.append(2)
llTwo.append(4)
llTwo.append(10)
llTwo.append(11)
llTwo.printList()

print("")

llOne.mergeSorted(llTwo)
llOne.printList()

print("")
llOne.removeDuplicates()
llOne.printList()