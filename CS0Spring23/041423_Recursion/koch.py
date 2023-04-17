def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

import turtle

turtle.setup(500,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Koch Fractal")     # Change the window title
wn.bgcolor("white")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
tess.backward(150)
tess.left(90) 

koch(tess, 4, 200)
tess.right(90)
koch(tess, 4, 200)
tess.right(90)
koch(tess, 4, 200)
tess.right(90)
koch(tess, 4, 200)
tess.right(90)

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()