import random, time


def mergesort(values):
    #Condition for exiting the recursion
    if len(values) == 1:
        return values
    
    left = values[:len(values)//2]
    right = values[len(values)//2:]

    left = mergesort(left)
    right = mergesort(right)

    return  merge(left,right)
    
def merge(list1, list2):
    list3 = []
    while len(list2) > 0 and len(list1) > 0 :
        if list1[0] < list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))

    if len(list2)>0:
        list3 += list2
    else :
        list3 += list1
        
    return list3


size = 1000
values = []

for i in range(size) :
    values.append(i)

print(values)
print(mergesort(values))

