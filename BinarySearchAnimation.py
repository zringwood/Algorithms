import random
import time
from AnimationRenderingWindow import ArrayWindow 

#Set up our display
values = range(400)
target = random.randint(0,len(values))
window = ArrayWindow((400,400),"Binary Search", values)

#Implements a basic binary search. 
low = 0
high = len(values)-1
index = (low + high)//2

#Update the highlights of the animation
window.highlights = [(target,(255,0,0)), (low,(0,0,255)), (high,(0,0,255))]
window.update()
while values[index] != target:
    if values[index] < target:
        low = index
    else:
        high = index
    index = (low + high)//2
    window.highlights = [(target,(255,0,0)), (low,(0,0,255)), (high,(0,0,255))]
    window.update()
    print("reached")
    time.sleep(1)
