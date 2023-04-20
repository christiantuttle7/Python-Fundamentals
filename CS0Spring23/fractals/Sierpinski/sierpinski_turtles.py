# Based off code for using tkinter to draw pixels found at
# https://gist.github.com/calebmadrigal/81f3b9de14f54ac355f7
# Instead of a sin wave, we will do a fractal, called among many names, Pascals triangle
# The algorythm is simple:
# 1) Decide the coordinates to define a triangle, which is baesed on our screen size. 
# We use the midpoint at the top and the bottom ends of the canvas
# 2) randomly choose one of those points
# 3) using ANY start coordinateds (x,y) calculate the midpoint between them and plot a pixel there.
# For less outliers untill the fractal falls into 
# repetition, I use one of the triangle points as a start, but experiment yourself!
# 4) Repeat. I've found a 1000x600 canvas fills in with 500000 iterations in 2-3 minutes. Start small...Maybe 10, and use print to debug
# We are using an inefficient library, but we don't have to worry about installing new modules. 

import random
import math
#from string import hexdigits
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop

width = 1100
height = 650
three_points = [[width/2, 0], [0, height-1], [width-1, height-1]]
iterations = 10000

window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000000")
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width//2, height//2), image=img, state="normal")
#xy = [random.randint(0,width-1) ,random.randint(0,height-1)]  #A random beginning point

def mid_point(point1, point2):
    mid_x = (point1[0]+point2[0])/2
    mid_y = (point1[1]+point2[1])/2
    return [mid_x, mid_y]

def rounded(a):
    return int(a+0.5)

def get_new_points(xy, num):
    next_points = []
    for i in range(num):
        next_choice = random.choice(three_points)
        new_point = mid_point(xy, next_choice)
        next_points.append(new_point)
        xy = new_point
        #assert(xy[0] >= 0 and xy[0] < width)
        #assert(xy[1] >= 0 and xy[1] < height)
    return next_points

def plot_points(f, iter):
    xy = three_points[1]
    points = f(xy, iter) 

    for p in points:
        x = rounded(p[0])
        y = rounded(p[1])
        red = (255*(y+1)//height)
        green = (255*(x+1)//width)
        blue = (int(255*math.sqrt(x**2 + y**2)+(math.sqrt((height-1)**2 + (width-1)**2))))
        #print("{:02x},{:02x},{:02x}".format(red,green,blue))
        #print( red, green, blue)        
        color = "#{:02x}{:02x}{:02x}".format(red,green,blue)  
        #print(color)  
        img.put(color, (x,y))
        

begin = time.time()
plot_points(get_new_points, iterations)
end = time.time()
diff = end - begin
minutes = int(diff//60)
seconds = diff%60
print("It took {:.3f} seconds, or {} minutes and {:.3f} seconds to draw {} points.".format(diff, minutes, seconds, iterations))
mainloop()

# Referenced from:
# https://gist.github.com/calebmadrigal/81f3b9de14f54ac355f7