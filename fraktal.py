import turtle as t

t.hideturtle()
t.left(90)

def fractal(size, branches):
    if branches > 0:
        t.forward(size)
        t.left(30)
    
        fractal(size*0.5, branches-1)

        t.right(60)
        
        fractal(size*0.5, branches-1)

        t.backward(size*0.5)


        


fractal(69, 6)        
    
