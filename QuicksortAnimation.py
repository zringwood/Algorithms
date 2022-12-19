import random, time

from AnimationRenderingWindow import ArrayWindow 

#helper method, shuffles the array
def shuffle(values):
    for i in range(len(values)-1):
        sav = values[i]
        randindex = random.randint(i,len(values)-1)
        values[i] = values[randindex]
        values[randindex] = sav

#Set up our display
values = list(range(400))
shuffle(values)
window = ArrayWindow((400,400),"Quicksort", values)
window.update()
    
def partition(values, low, high):
    pivot = values[high]
    pivindex = high
    i = low
    while i < pivindex:
        #If it's greater than the pivot, insert it one after the pivot
        if values[i] > pivot:
            save = values.pop(i)
            values.insert(pivindex,save)
            pivindex -=1
            window.update()
        else:
            i+=1
    return pivindex
def quicksort(values, low,high):
    #Exit condition for the recursion
    if low >= high or low < 0 :
        return
    
    pivot = partition(values,low,high)
    quicksort(values,low,pivot-1) #left of the pivot
    quicksort(values,pivot+1,high) #right side of the pivot
    

quicksort(values,0,len(values)-1)
time.sleep(3)
window.quit()
