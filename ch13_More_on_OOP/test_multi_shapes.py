from MovingShapes import *
frame = Frame()

numshapes = 3
shapes = []

size = 50

for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))
    

for i in range(100):
    for shape in shapes:
        shape.moveTick()

frame.close()
    

