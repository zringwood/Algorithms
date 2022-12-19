import random
import time
from ArrayRenderingWindow import ArrayWindow 

#Set up our display
values = range(400)
target = random.randint(0,len(values))
window = ArrayWindow("Binary Search", values)

#Implements a basic binary search. 
low = 0
high = len(values)-1
index = (low + high)//2

#Update the highlights of the animation
window.highlights = [(target,"red"), (low,"white"), (high,"white")]
window.nextframe()
while values[index] != target:
    if values[index] < target:
        low = index
    else:
        high = index
    index = (low + high)//2
    window.highlights = [(target,"red"), (low,"white"), (high,"white")]
    window.nextframe()
    time.sleep(1)
