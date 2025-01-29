import pygame

pygame.init()
#widon dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
#Creates game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Window caption
pygame.display.set_caption("Cookie Clicker")

running = True
#loop to keep game window open as long as running = true
while running:
    #For all mouse clicks and key presses and window close
    for event in pygame.event.get():
        #When the x button on the top left is clicked it exits out
        if event.type == pygame.QUIT:
            running = False
    # Game window color of the pop up game/tab
    screen.fill((0, 100, 100))
    #update display
    pygame.display.flip()
pygame.quit()

clock = pygame.time.Clock()
clock.tick(60)