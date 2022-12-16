import random, time

def mergesort(values):
    #Condition for exiting the recursion
    if len(values) == 1:
        #Lists of length 1 are sorted by definition
        return values

    #Divide the list into two
    left = values[:len(values)//2]
    right = values[len(values)//2:]

    #Recursion
    left = mergesort(left)
    right = mergesort(right)

    #Will return a sorted list as long as left and right are both sorted
    return  merge(left,right)

#Combines two sorted lists and returns a list containing all elements from both
#in ascending order. 
def merge(list1, list2):
    #Buffer
    list3 = []
    #Continue until one of the lists is empty
    while len(list2) > 0 and len(list1) > 0 :
        if list1[0] < list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    
    #One of the lists will still have elements that need to be added. 
    if len(list2)>0:
        list3 += list2
    else :
        list3 += list1
        
    return list3


size = 10
values = []

for i in range(size) :
    values.append(random.randint(0,size))

print(values)
print(mergesort(values))

