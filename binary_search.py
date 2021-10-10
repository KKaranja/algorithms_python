def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2


        if list [midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target Found at index: ", index) 
    else:
        print("Target not found in the list") 


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

result = binary_search(numbers, 38)
verify (result)

result = binary_search(numbers, 28)
verify (result)
