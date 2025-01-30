import pygame

pygame.init()
#widon dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

#Creates game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Window caption
pygame.display.set_caption("Cookie Clicker")


# Load the cookie image and set its size
cookie_image = pygame.image.load("cookie.png")
cookie_size = (100, 100)  # Width and height in pixels
cookie_image = pygame.transform.scale(cookie_image, cookie_size)

#initial cookie position
cookie_x = 250  # Center horizontally 
cookie_y = 150  # Center vertically

# the font the the display score will have
font = pygame.font.SysFont("Arial", 30)  # Font name and size
score = 0 #give the score a value to begin with



running = True
#loop to keep game window open as long as running = true
while running:
    #For all mouse clicks and key presses and window close
    for event in pygame.event.get():
        #When the x button on the top left is clicked it exits out
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.fill((255, 0, 0))
                    # Check if the click is on the cookie
            if (cookie_x <= mouse_x <= cookie_x + cookie_size[0] and
                    cookie_y <= mouse_y <= cookie_y + cookie_size[1]):
                score += 1  # Increment the score
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                running = False
    # Game window color of the pop up game/tab
    screen.fill((0, 100, 100))
    #game loop speed into 60 frames per sec
    clock = pygame.time.Clock()
    clock.tick(60)


        # Draw the cookie on the screen
    screen.blit(cookie_image, (cookie_x, cookie_y))
    # Render the score text
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # Black color
    screen.blit(score_text, (10, 10))  # Display at the top-left corner



    
    #update display
    pygame.display.flip()
pygame.quit()