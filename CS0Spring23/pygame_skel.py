import pygame, math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 800
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()

def gameloop():
    
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            return

        # Draw everything
        main_surface.fill((30, 0, 30)) #fill background color
        # Draw stuff
        color = (0,255,0)
        p1 = (0,0)
        p2 = (surface_size,surface_size)
        pygame.draw.line(main_surface, color, p1, p2)
        
        pygame.display.flip() # Put all the drawing up to the display
        my_clock.tick(120) #Keeps a contant framerate for smoother animation
        # If you don't include the above line, the loop executes as fast as it can

gameloop()
pygame.quit()