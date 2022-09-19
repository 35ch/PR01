from turtle import *

hideturtle()
speed(1)

n = 0
n1 = 1

rng = int(input())

for i in range(rng):
    print(n)
    print(n1)
    
    n += n1
   
    for r in range(6):
        left(90)
        if i%2==True:
            forward(10*n)
        else:
            forward(10*n1)
    
    left(90)

    for o in range(6):
        left(90)
        if i%2==True:
            forward(10*n1)
        else:
            forward(10*n)

    n1 += n

input()
