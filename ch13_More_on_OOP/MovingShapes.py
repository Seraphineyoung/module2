from pylab import random as r
from Shapes import *

#cordx = starting x position
#cordy = starting y position
#deltax,deltay  = Instance variable that randomly generates a number between 0 and 15 
#min_x,max_y = Holds the minimum starting position of Xand Y, which is within the diameter of the box.
#min_y,Max_y = Holds the minimum starting position of Xand Y, which is within the diameter of the box.


class MovingShape:
    def __init__(self,frame,shape,diameter,cordx=0,cordy=0,min_x=0,max_x=0,min_y=0,max_y=0,deltax = 5+10 * r(),deltay = 5+10 * r()):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        #Intializing the frame class in order to access the width 
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
        #generation a random value for starting position of Y
        self.cordx = self.min_x + r() * (self.max_x - self.min_x )
        
        
    def mininum_position_Y(self):
        self.min_y = self.diameter/2
        self.max_y = self.frame.height - self.min_y
        #generation a random value for starting position of Y
        self.cordy = self.min_y + r() * (self.max_y - self.min_y )
        
        
    def call_minX_and_minY(self):
        self.mininum_position_X()
        self.mininum_position_Y()
        
              
                     
    def moveTick(self): 
        
         self.call_minX_and_minY()
         
         self.cordx = self.cordx + self.deltax 
         self.cordy = self.cordy + self.deltay
          
         if self.cordx < self.min_x or self.cordx > self.max_x:
             self.cordx = self.cordx * -1
             
         if self.cordy < self.min_y or self.cordy > self.max_y:
               self.cordy = self.cordy * -1 
               
         self.goto(self.cordx,self.cordy)
         
    
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        
class Diamond(MovingShape):
    
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        
    def mininum_position_diamond_X(self):
        self.min_x = self.diameter * 2
        
        self.max_x = self.frame.width - self.min_x
        #generation a random value for starting position of Y
        self.cordx = self.min_x + r() * (self.max_x - self.min_x )
        
        
    def mininum_position_diamond_Y(self):
        self.min_y = self.diameter * 2
        
        self.max_y = self.frame.height - self.min_y
        #generation a random value for starting position of Y
        self.cordy = self.min_y + r() * (self.max_y - self.min_y )
        
        
    def call_minX_and_minY(self):
        self.mininum_position_diamond_X()
        self.mininum_position_diamond_Y()
        
        
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
    
class Polygon(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'polygon',diameter)
        
    
        
        
        