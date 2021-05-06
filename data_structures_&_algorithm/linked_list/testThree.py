import CustomLinkedList

llOne = CustomLinkedList.LinkedList()
llOne.append(1)
llOne.append(2)
llOne.append(3)
llOne.append(2)
llOne.append(1)
llOne.printList()

print("")
print(llOne.isPalindromeOne()) # should return True
print(llOne.isPalindromeTwo()) # should return True
print(llOne.isPalindromeThree()) # should return True

print("")
llOne.append(1)
print(llOne.isPalindromeOne()) # should return False
print(llOne.isPalindromeTwo()) # should return False
print(llOne.isPalindromeThree()) # should return False