import pygame
import random

def mid_point(p1, p2):
    x = (p1[0] + p2[0])/2
    y = (p1[1] + p2[1])/2
    return [x,y]  

pygame.init()
width = 1600
height = 900
iterations = 100

p0 = [width/2, 0]
p1 = [0, height-1]
p2 = [width-1, height-1]
tri_points0 = [p0, p1, p2]
xy = p0

window = pygame.display.set_mode((width, height))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if(event.key == pygame.K_ESCAPE):
                run = False

    #window.fill(0)

    #rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size())//2]*2))
    for i in range(iterations):
    
        point = random.choice(tri_points0)
        mid = mid_point(point, xy)
        xy = mid
        u = xy[0] / (width - 1)
        w = xy[1] / (height - 1)
        color = (round(u*255), round(w*255), round((1-u)*255))
        window.set_at((int(xy[0]), int(xy[1])), color)

    #for x in range(1000):
    #    u = x / (1000 - 1)
    #    color = (round(u*255), round(u*255), round((1-u)*255))
    #    for y in range(800):
    #        window.set_at((x, y), color) 
    
    pygame.display.flip()

pygame.quit()
exit()