from MovingShapes import *
frame = Frame()

numshapes = 5
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame,100))
    
for i in range(50):
    for shape in shapes:
        shape.moveTick()