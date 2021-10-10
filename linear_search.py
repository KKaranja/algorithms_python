def linear_search(list, target):
    """
    returns the index position of the target if found, else return none.
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i

    return None

def verify(index):
    if index is not None:
        print("Target Found at index: ", index) 
    else:
        print("Target not found in the list")           

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

result = linear_search(numbers, 38)
verify (result)

result = linear_search(numbers, 28)
verify (result)