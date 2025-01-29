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
    #game loop speed into 60 frames per sec
    clock = pygame.time.Clock()
    clock.tick(60)

    # Load the cookie image and set its size
    cookie_image = pygame.image.load("cookie.png")
    cookie_size = (100, 100)  # Width and height in pixels
    cookie_image = pygame.transform.scale(cookie_image, cookie_size)

    # Set the initial position of the cookie
    cookie_x = 250  # Center horizontally (adjust based on window size)
    cookie_y = 150  # Center vertically (adjust based on window size)
        # Draw the cookie on the screen
    screen.blit(cookie_image, (cookie_x, cookie_y))
    #update display
    pygame.display.flip()
pygame.quit()