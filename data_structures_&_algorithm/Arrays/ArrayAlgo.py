
# PROBLEM ONE - ARRAY ADVANCE GAME

# rule: Is it possible to advance from the start of the array to the last element given that the maximum you 
#       ...can advance from a position is based on the value of the array at the index you are currently present on?
# link: https://www.educative.io/courses/ds-and-algorithms-in-python/qZO32VLk0xr
def isWinnable(arrayList):
    indexLength = len(arrayList) - 1
        
    maxNum = 0
        
    for i in range(indexLength):
        maxNum = max(maxNum, arrayList[i] + i)
        print(maxNum)
        if (maxNum <= i):
            return False
        if (maxNum >= indexLength):
            return True

# winnable
winnableOne = [3,3,1,0,2,0,1]
winnableTwo = [2,4,1,1,0,2,3]

# unwinnable
unwinnableOne = [3,2,0,0,2,0,1]

# should return True
print(isWinnable(winnableOne))
print(isWinnable(winnableTwo))
print("")

# should return False
print(isWinnable(unwinnableOne))
print("")


# PROBLEM TWO - ARBITRARY PRECISION INCREMENT

# Given: An array of non-negative digits that represent a decimal integer.
# Problem: Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.
# link: https://www.educative.io/courses/ds-and-algorithms-in-python/qAxkGJ0lxmG

def plusOneA(arrayList):
    
    carry = 1
    answer = list()
    
    for num in arrayList[::-1]:
        tempNum = (num + carry)
        answer.insert(0, (tempNum % 10))
        carry = tempNum // 10
    
    if (carry > 0):
        answer.insert(0, carry)
        
    return answer

def plusOneB(arrayList):
    s = "".join(map(str, arrayList))
    print(int(s) + 1)
    
def plusOneC(arrayList):
    arrayList[-1] += 1
    for i in reversed(range(1,len(arrayList))):
        if arrayList[i] != 10:
            break
        arrayList[i] = 0
        arrayList[i-1] += 1
    if (arrayList[0] == 10):
        arrayList[0] = 1
        arrayList.append(0)
    return arrayList

# all the the following should return True
print(plusOneA([9,9,9]) == [1,0,0,0])
print(plusOneA([0]) == [1])
print(plusOneA([1,2,5]) == [1,2,6])
print(plusOneA([9]) == [1,0])

print("")
print(plusOneC([9,9,9]) == [1,0,0,0])
print(plusOneC([0]) == [1])
print(plusOneC([1,2,5]) == [1,2,6])
print(plusOneC([9]) == [1,0])