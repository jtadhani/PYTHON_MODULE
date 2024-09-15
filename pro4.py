li = [10,14,20,22,28,38,42,47]
value = int(input("Enter the number of search :- "))

def binary_search(li , value):

    low = 0
    high = len(li) - 1

    while low <= high:

        mid = (low + high) // 2

        if li[mid] == value:
            return mid
        elif li[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1

bs = binary_search(li , value)

if bs == -1:
    print("value is not found in the list")
else:
    print(f"{value} is found at index {bs}")