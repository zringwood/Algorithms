import random
import time

#Implements a basic binary search. 
def search(values, target):
    low = 0
    high = len(values)
    index = (low + high)//2
    while values[index] != target:
        if values[index] < target:
            low = index
        else:
            high = index
        index = (low + high)//2
        print("Low: {} High: {} Index: {}".format(low,high,index))
        time.sleep(0.5)
        

#Implement some kind of slider for this.
size = (int)(1e6)
values = range(size)
target = (int)(random.random()*size)

print(target)
search(values, target)
