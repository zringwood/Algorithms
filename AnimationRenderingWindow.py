import pygame, random, time

#Assistance class for drawing arrays to a surface as a series of lines.
class ArrayWindow():
    def __init__(self,size,title,array): 
        pygame.init()
        self.size = size
        self.array = array
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        #The highlights is a list of tuples containing the index to be highlighted
        #and the color for it to be highlighted in.
        self.highlights = []
        self.update()
    #Draws the array one additional time. 
    def update(self):
        #Clear the screen
        self.screen.fill((0,0,0))
        #Array of values we're going to draw as lines on the screen.
        for i in self.array :
            pygame.draw.line(self.screen, (255,255,255), (i,self.size[0]),(i,self.size[0]-self.array[i]))
        for i in self.highlights :
            pygame.draw.line(self.screen, i[1], (i[0],self.size[0]),(i[0],self.size[0]-self.array[i[0]]))
        pygame.display.update()

    #helper method, shuffles the array
    def shuffle(self, animate):
        array = self.array
        for i in range(len(array)-1):
            sav = array[i]
            randindex = random.randint(i,len(array)-1)
            array[i] = array[randindex]
            array[randindex] = sav
            if animate:
                self.update()

window = ArrayWindow((400,400),"Test",list(range(400)))
window.highlights = [(random.randint(0,400),(255,0,0)),(random.randint(0,400),(255,0,0)),(random.randint(0,400),(255,0,0))]
#window.shuffle(True)
window.update()
