from MovingShapes import *
frame = Frame()

numshapes = 5
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame,100))
    
for i in range(200):
    for shape in shapes:
        shape.moveTick()