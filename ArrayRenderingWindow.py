#This is an assistance class meant to draw arrays clearly.
#It is useful for displaying sorting algorithms.
from graphics import *
import time

class ArrayWindow(GraphWin):
    def __init__(self, title, array):
        super().__init__(title, 400,400,False)
        self.size = 400
        #Bottom Left of the canvas treated as 0,0
        self.setCoords(0, 0, self.size, self.size)
        #The array that will be displayed in the center of the window
        self.array = array
        #Takes an array of indicies that will be drawn in a different colour to
        #to the rest of the array. Defaults to white. 
        self.highlights = []
        
        
    #Used for animations. Clears out the screen. 
    def clear(self):
        bgrect = Rectangle(Point(0,0),Point(self.size,self.size))
        bgrect.setFill(color_rgb(164, 166, 159))
        bgrect.draw(self)
    #This method clears the window and draws the next frame of the animation.
    def nextframe(self):
        self.clear()
        barwidth = self.size // len(self.array)
        print(barwidth)
        #The array is drawn as a series of bars. 
        for i in range(len(self.array)) :
            bar = Rectangle(Point(i*barwidth,0), Point(i*barwidth+barwidth,self.array[i]))
            if self.highlights.count(i) > 0 :
                bar.setFill("black")
            else:
                bar.setFill("white")
            bar.draw(self)
        #This needs to be called at the end in order for the animation to work properly. 
        self.update()


