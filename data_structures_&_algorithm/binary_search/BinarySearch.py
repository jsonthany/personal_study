def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
    
        if data[mid] == target:
            return True
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        
        return binary_search_recursive(data, target, low, high)
    
def find_closest_num_jt(A, target):
    low = 0
    high = len(A) - 1
    current = float("inf")
    
    if len(A) == 1:
        return A[0]
    if len(A) == 0:
        return None
    
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] == target:
            return A[mid]
        elif A[mid] < target:
            if mid+1 < len(A):
                current = best_of_pair(A[mid], A[mid+1], current, target)
            low = mid + 1
        else:
            if mid > 0:
                current = best_of_pair(A[mid], A[mid-1], current, target)
            high = mid -1
            
    return current
            
def best_of_pair(a, b, c, target):
    if abs(target - a) <= abs(target - b) and abs(target - a) <= abs(target - c):
        return a
    elif abs(target - b) <= abs(target - a) and abs(target - b) <= abs(target - b):
        return b
    else:
        return c


def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    # Edge cases for empty list of list
    # with only one element:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high)//2

        # Ensure you do not read beyond the bounds
        # of the list.
        if mid+1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        # Check if the absolute value between left
        # and right elements are smaller than any
        # seen prior.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        # Move the mid-point appropriately as is done
        # via binary search.
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
        # If the element itself is the target, the closest
        # number to it is itself. Return the number.
        else:
            return A[mid]
    return closest_num

def find_fixed_point(A):
    low = 0
    high = len(A) - 1
    
    while (low <= high):
        mid = (low + high) // 2
        
        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
        
    return None

def find_highest_number(A):
    low = 0
    high = len(A) - 1
    
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
        
        if (mid < len(A) - 1) and (mid > 0):
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return A[mid]
            elif A[mid] < A[mid - 1]:
                high = mid - 1
            elif A[mid] < A[mid + 1]:
                low = mid + 1
                
        if (mid == 0):
            if A[mid] > A[mid + 1]:
                return A[mid]
        if (mid == len(A)-1):
            if A[mid] > A[mid - 1]:
                return A[mid]
                
    return None


                
def find(A, target):
    low = 0
    high = len(A) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if (A[mid] == target):
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

def integer_square_root(k):
    
    low = 0
    high = k 

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1



data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37

print(binary_search_recursive(data, target, 0, len(data)-1))
print(binary_search_iterative(data, target))

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]
A3 = [1, 4, 7, 12, 45, 78, 1000, 2340, 10000]

print(find_closest_num_jt(A1, 11))
print(find_closest_num_jt(A2, 4))
print(find_closest_num_jt(A3, 0))
print(find_closest_num_jt([5], 0))
print(find_closest_num_jt([], 0))

print(find_closest_num(A1, 11))
print(find_closest_num(A2, 4))
print(find_closest_num(A3, 0))
print(find_closest_num([5], 0))
print(find_closest_num([], 0))

# Fixed point is 3:
A4 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A5 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A6 = [-10, -5, 3, 4, 7, 9]


print("Binary Search Approach")
print(A4)
print(find_fixed_point(A4))
print(A5)
print(find_fixed_point(A5))
print(A6)
print(find_fixed_point(A6))

A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find(A, target)
print(x)