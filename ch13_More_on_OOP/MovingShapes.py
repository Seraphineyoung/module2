
from Shapes import *
from pylab import random as r


class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.frame = frame
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.minxy = self.diameter/2
        self.maxx = self.frame.width - self.minxy
        self.maxy = self.frame.height - self.minxy
        self.x = self.min_x + r() * (self.max_x - self.min_x )
        self.y = self.min_y + r() * (self.max_y - self.min_y )
        self.dx = 5 + 10 * r() 
        self.dy = 5 + 10 * r() 
        self.goto(self.x, self.y)
        
    def goto(self, x, y):
        self.figure.goto(x, y)
        
    def moveTick(self):
        if self.x > self.maxx:
            self.dx = (1 - 10) * random.random()
        elif self.x < self.minxy:
            self.dx = (1 + 10) * random.random()
        else:
            pass       
        
        self.x += self.dx
        
        if self.y > self.maxy:
            self.dy = (1 - 10) * random.random()
        elif self.y < self.minxy:
            self.dy = (1 + 10) * random.random()
        else:
            pass
        
        self.y += self.dy
        
        self.figure.goto(self.x, self.y)
    
        
#    def __init__(self,frame,shape,diameter):
#        
#        self.shape = shape
#        self.diameter = diameter
#        self.figure = Shape(shape,diameter)
#        self.frame = frame
#        self.move_positions()
#
#
#        self.cordx = self.min_x + r() * (self.max_x - self.min_x )
#        self.cordy = self.min_y + r() * (self.max_y - self.min_y ) 
#        
#        print(self.min_x)
#        print(self.min_x)
#        print(self.max_y)
#        print(self.min_y)
#        
#        self.deltax = 5 + 10 * r()    
#
#        self.deltay = 5 + 10 * r()
#
#        if r() < 0.5:
#            self.deltay = 5 + 10 * r()
#            self.deltax = 5 + 10 * r()
#        else:
#            self.deltay = -5 + -10 * r() 
#            self.deltax = -5 + -10 * r()
#            
#
#    def move_positions(self):
#            
#        self.min_x = self.diameter/2
#        self.max_x = self.frame.width - self.min_x
#        self.min_y = self.diameter/2
#        self.max_y = self.frame.height - self.min_y
#              
#        
#        
#    def goto(self,x,y):
#            self.figure.goto(x,y)
#            
#            
#    def moveTick(self):
#
##        self.cordx= self.cordx + self.deltax
##        self.cordy= self.cordy + self.deltay
##        self.figure.goto(self.cordx,self.cordy)
##
##        
##       
##        if self.cordx < self.min_x:
##            self.deltax = self.deltax * -1
##            
##        if self.cordy < self.min_y:
##            self.deltay = self.deltay * -1
##            
##        if self.cordx > self.max_x:
##            self.deltax = self.deltax * -1
##            
##        if self.cordy > self.max_y:
##            self.deltay = self.deltay * -1
#        
#        
#        if self.cordx<=self.min_x or self.cordx>=self.max_x: 
#            self.deltay =- self.deltay 
#        if self.cordy<=self.min_y or self.cordy>=self.max_y:
#            self.deltay=-self.deltay 
#            
#        self.cordx +=  self.deltax
#        self.cordy +=  self.deltay
#        self.goto(self.cordx,self.cordy)
         

        
    
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
    

        
    
        
        
        