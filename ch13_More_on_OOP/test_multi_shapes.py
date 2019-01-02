from MovingShapes import *
frame = Frame()

numshapes = 3
shapes = []

size = 70

for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))
    #shapes.append(Polygon(frame,size))

for i in range(20):
    for shape in shapes:
        shape.moveTick()

frame.close()
    

#for i in range(numshapes):
#    shapes.append(Square(frame,100))
#    
#for i in range(50):
#    for shape in shapes:
#        shape.moveTick()