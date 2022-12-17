import random, time

def quicksort(values):
    #Exit condition for the recursion
    if len(values) <= 1:
        return values
    pivot = values[-1]
    greater, lesser = [],[]
    #Split the array around the pivot
    for i in values :
        if i > pivot :
            greater.append(i)
        else :
            lesser.append(i)
    #The algorithm will keep selecting the same pivot if it stays in lesser
    lesser.pop(len(lesser)-1)
    return quicksort(lesser) +[pivot]+ quicksort(greater)

size = 100
values = []

for i in range(size) :
    values.append(random.randint(0,size))

print(values)
print(quicksort(values))


    
