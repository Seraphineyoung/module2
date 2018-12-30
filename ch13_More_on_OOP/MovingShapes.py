from pylab import random as r
from Shapes import *

class MovingShape:
    def __init__(self,frame,shape,diameter,cordx = 0,cordy= 0,min_x=0,max_x=0,min_y=0,max_y=0,deltax = 5+10 * r(),deltay = 5+10 * r()):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        self.frame = frame
        self.cordx = cordx
        self.cordy = cordy
        self.deltax = deltax
        self.deltay = deltay
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        
        
    def goto(self,x,y):
        self.figure.goto(x,y)
        
        
    def mininum_position_X(self):
        self.min_x = self.diameter/2
        self.max_x = self.frame.width - self.min_x
        self.cordx = self.min_x + r() * (self.max_x - self.min_x )
        
        
   
    def mininum_position_Y(self):
        self.min_y = self.diameter/2
        self.max_y = self.frame.width - self.min_y
        #generation a random value for starting position of Y
        self.cordy = self.min_y + r() * (self.max_y - self.min_y )
        
       
               
    def moveTick(self):
         self.mininum_position_X()
         self.mininum_position_Y()
         self.cordx += self.cordx + self.deltax
         self.cordy += self.cordy + self.deltay
         self.goto(self.cordx,self.cordy)
         
    
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
        
        
        
        