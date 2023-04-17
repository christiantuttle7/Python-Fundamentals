import turtle

def koch(taya, length, order):
    if(order == 0):
        taya.forward(length)
    else:
        koch(taya, length/3, order-1)
        taya.left(60)
        koch(taya, length/3, order-1)
        taya.right(120)
        koch(taya, length/3, order-1)
        taya.left(60)
        koch(taya, length/3, order-1)




turtle.setup(500,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Koch Fractal")     # Change the window title
wn.bgcolor("white")             # Set the background color

taya = turtle.Turtle()               # Create our favorite turtle

taya.backward(250)
taya.color('green')

koch(taya, 500, 2)

wn.mainloop()