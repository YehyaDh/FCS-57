def BinarySearch(list,start,end,key):
    # base case
    if start >= end:
        return -1   
    else:
        mid = (start + end) // 2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            return BinarySearch(list,start,mid-1,key)
        else:
            return BinarySearch(list,mid+1,end,key)

    
    
# test of the function

list1 = [1, 4, 7, 8, 20, 22, 44, 90, 100]  # sorted list
result = BinarySearch(list1, 0, len(list1)-1, 100)
if result != -1:
    print("Found")
else:
    print("Not Found")