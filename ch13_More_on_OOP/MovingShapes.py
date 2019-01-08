
from Shapes import *
from pylab import random as r


class MovingShape:

    def __init__(self,frame,shape,diameter):
        
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        self.frame = frame
        
        self.min_xy, self.max_xy = self.move_positions()
        
        ran_gen = r()

        self.cordx = self.min_xy + r() * (self.max_xy - self.min_xy )
        self.cordy = self.min_xy + r() * (self.max_xy - self.min_xy )
        
        

        
        self.deltax = 5 + 10 * r()    

        self.deltay = 5 + 10 * r()

        if ran_gen < 0.5:
            
            self.deltay = 5 + 10 * ran_gen
            self.deltax = 5 + 10 * ran_gen
        else:
            self.deltay = 5 + 10 * -ran_gen 
            self.deltax = 5 + 10 * -ran_gen
            
        

    def move_positions(self):
            
        self.min_xy = self.diameter
        
        self.max_xy = self.frame.width - self.min_xy
        
        return self.min_xy , self.max_xy

        
        
    def goto(self,x,y):
            self.figure.goto(x,y)
            
            
    def moveTick(self):

        ran_gen = r()
        if self.cordx <= self.min_xy:
            print(self.cordx,self.min_xy,'a')
            self.deltax = (5 + 10 * ran_gen)
                
            
        elif self.cordy <= self.min_xy:
            print(self.cordy,self.min_xy,'b')
            self.deltay = (5 + 10 * ran_gen)
            print(self.deltay)
            
        elif self.cordx >= self.max_xy:
            print(self.cordx,self.max_xy,'c')
            self.deltax = (-5 + 10 * -ran_gen)
            print(self.deltax)
            
        elif self.cordy >= self.max_xy:
            print(self.cordy,self.max_xy,'d')
            self.deltay = (-5 + 10 * -ran_gen)
            print(self.deltay)
            
        self.cordx += self.deltax
        print(self.cordx,'x')
        self.cordy += self.deltay
        print(self.cordy,'y')
        
        self.goto(self.cordx,self.cordy)

         

        
    
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        
class Diamond(MovingShape):
    
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)

        
        def move_positions(self):
            
            self.min_xy = self.diameter
            self.max_xy = self.frame.width - self.min_xy
            return self.min_xy , self.max_xy
        
        
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
    

        
    
        
        
        