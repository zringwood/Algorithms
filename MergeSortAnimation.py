import random, time
from AnimationRenderingWindow import ArrayWindow

values = list(range(400))
#Initialize our display
window = ArrayWindow((400,400),"Merge Sort",values)
window.shuffle(True)

#This implementation of mergesort needs to change the original array.
#"low" and "high" define the range of values to influence
def mergesort(values, low, high):
    #Condition for exiting the recursion
    if high - low == 1:
        #Lists of length 1 are sorted by definition
        return (low,high)

    #Recursion left
    mergesort(values, low,(high+low)//2)
    #Recursion right
    mergesort(values, (high+low)//2, high)
    
    #Will return a sorted list as long as left and right are both sorted
    merge(values, (low,(high+low)//2), ((high+low)//2, high))
    window.update()

#Combines two sorted lists and returns a list containing all elements from both
#in ascending order.
#This method assumes the two sub-lists are adjacent in the master list. 
def merge(values, listindices_0,listindices_1):
    lo_0, hi_0 = listindices_0[0], listindices_0[1]
    lo_1, hi_1 = listindices_1[0], listindices_1[1]
    #These indices iterate independently over the parts of the array we're merging
    index_0, index_1 = lo_0, lo_1
    #This buffer stores the integers until we're ready to add them to values
    buffer = []
    #Continue until one of the indicies is complete
    while index_0 < hi_0 and index_1 < hi_1 :
        if values[index_0] < values[index_1]:
            buffer.append(values[index_0])
            index_0 += 1
        else:
            buffer.append(values[index_1])
            index_1 += 1
    
    #There will still be elements that need to be added. 
    while index_0 < hi_0:
        buffer.append(values[index_0])
        index_0 += 1
    while index_1 < hi_1:
        buffer.append(values[index_1])
        index_1 += 1    
    #Finally, remove the values we've merged and add the buffer to values
    for i in range(hi_1-lo_0):
        values[lo_0 + i] = buffer[i]
        window.update()

mergesort(values,0,len(values))
time.sleep(3)
window.quit()
