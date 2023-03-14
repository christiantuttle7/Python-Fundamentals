# pick a point
# randomly choose a vertix of the triangle
# calculate the point halfway between the starting point and the guess
# plot a point halfway between the triangle vertix and the original position
# from the new position, repeat

import pygame
import random

def find_mid_point(p1, p2):
    x_mid = int((p1[0]+p2[0])/2)
    y_mid = int((p1[1]+p2[1])/2)

    return (x_mid, y_mid)


pygame.init()
width = 1600
height = 900
iterations = 10000

triangle_point = [(0, height/3), (width/2, 0), (width-1, height/3), (0, height*2/3), (width/2,height-1), (width-1, height*2/3), (width/2, height/2)]

#xy = (random.randint(0,width-1), random.randint(0,height-1))
xy = triangle_point[0]

window = pygame.display.set_mode((width, height))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if(event.key == pygame.K_ESCAPE):
                run = False
    
    for i in range(iterations):
        guess_point = random.choice(triangle_point)
        mid_point = find_mid_point(xy, guess_point)

        #red = random.randint(0,255)
        red = mid_point[0]/width * 255
        green = mid_point[1]/height * 255

        b_scale = (255/(height+width))
        blue = (mid_point[0]+mid_point[1])*b_scale

        color = (red,green,255-blue)
        window.set_at(mid_point, color) #Plot a pixel at (mid_point[0],mid_point[1])
        xy = mid_point
    
    pygame.display.flip()

pygame.quit()
exit()