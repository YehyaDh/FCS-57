def insertSort(list1,val):
    for i in range(len(list1)):
        tmp=list[i]
        if tmp>=val:
            list1.insert(i,val)
            return list1
        
# Testing the function

list=[1,34,56,78,89]
val=77

result=insertSort(list,val)
print(result)

list=[1,3,56,234,789]
val=-99

result=insertSort(list,val)
print(result)

list=[1,3,56,234,789]
val=789

result=insertSort(list,val)
print(result)