import pygame, math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 800
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()

def koch(start, heading, angle, order, size):

    color = (0,255,0)
    p1 = start
    p2 = ()
    p2_x = p1[0] + size*math.cos((heading+angle)*math.pi/180)
    p2_y = p1[1] + size*math.sin((heading+angle)*math.pi/180)
    p2 = (p2_x, p2_y)    
    if order == 0:
        pygame.draw.line(main_surface, color, p1, p2)
        pygame.display.flip()
        return p2
    if(order > 0):
        p2 = start
        for angles in [0, -60, 120, -60]:
            angle += angles
            p2 = koch(p2, heading, angle, order-1, size/3)
        return p2
        #   t.left(angle)

def gameloop():

    #while True:

    # Handle evente from keyboard, mouse, etc.
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        return

        # Draw everything
        #main_surface.fill((30, 0, 30)) #fill background color
        # Draw stuff
        #color = (0,255,0)
        #p1 = (0,0)
        #p2 = (surface_size,surface_size)
        #pygame.draw.line(main_surface, color, p1, p2)
    koch((surface_size*0.05, surface_size//2), 0, 0, 6, surface_size*0.9)

    pygame.display.flip() # Put all the drawing up to the display
    my_clock.tick(120) #Keeps a contant framerate for smoother animation
        # If you don't include the above line, the loop executes as fast as it can


gameloop()
pygame.quit()