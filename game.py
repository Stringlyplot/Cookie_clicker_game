import pygame
import random

pygame.init()
#widon dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

#Creates game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Window caption
pygame.display.set_caption("Cookie Clicker")
#game loop speed into 60 frames per sec
clock = pygame.time.Clock()



# Load the cookie image and set its size
cookie_image = pygame.image.load("cookie.png")
cookie_size = (200, 200)  # Width and height in pixels
cookie_image = pygame.transform.scale(cookie_image, cookie_size)

#initial cookie position
cookie_x = 200  # Center horizontally 
cookie_y = 90  # Center vertically

#Cookie upgrade variable
cookies_per_second = 0
upgrade_cost = 50

# the font the the display score will have
font = pygame.font.SysFont("Arial", 30)  # Font name and size
score = 0 #give the score a value to begin with

#Upgrade button location and dimension
button_x = 400
button_y = 300
button_width = 150
button_height = 50

#timer setup for auto-incremnting cookies
clock = pygame.time.Clock()
AUTO_INCREMENT_INTERVAL = 1000
last_auto_increment = pygame.time.get_ticks()
#intalizes our Varaible for number of upgrades
num_upgrades = 0

#Where the effects get stored a list
fade_effects = []

#The initial variable for our animation
cookie_bounce = {"scale": .9, "direction": 1}


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

                    # Check if the click is on the cookie
            if (cookie_x <= mouse_x <= cookie_x + cookie_size[0] and
                    cookie_y <= mouse_y <= cookie_y + cookie_size[1]):
                score += 1  # Increment the score
                cookie_x = random.randint(0, WINDOW_WIDTH - cookie_size[0])
                cookie_y = random.randint(0, WINDOW_HEIGHT - cookie_size[1])
                cookie_bounce["direction"] = -1 #Shrinks the cookie
                fade_effects.append({"x": mouse_x, "y": mouse_y, "radius": 10, "alpha": 255})  # Start a fade effect


            elif (button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height):
                if score >= upgrade_cost: #upgrade is 50 cookies:
                    score -= upgrade_cost  # takes 50 from cookies
                    num_upgrades += 1
                    cookies_per_second +=1
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                running = False


    # background color for window color of the pop up game/tab
    screen.fill((194, 180, 78))
    clock.tick(60)

    # Draw the cookie on the screen

    # Render the score text
    score_text = font.render(f"Score: {score}", True, (50, 50, 120))  # Black color
    screen.blit(score_text, (10, 10))  # Display at the top-left corner
    #drawing ugrade button  This is the color
    pygame.draw.rect(screen, (0, 200, 0), (button_x, button_y, button_width, button_height))
    button_text = font.render("Upgrade", True, (255, 255, 255))
    screen.blit(button_text, (button_x + 20, button_y + 10))

    #display upgrade cost
    cost_text = font.render(f"Cost: {upgrade_cost}", True, (200,30,30))
    screen.blit(cost_text, (button_x, button_y - 30))
    #Display the umber of upgrades purchased
    upgrades_text = font.render(f"Upgrades:{num_upgrades}", True, (30,60,30)) # Black upgrade text
    screen.blit(upgrades_text, (button_x, button_y + button_height + 10))  # Below the button
    #Increases the cost of the upgrade button everytime its clicked
    upgrade_cost = int(50 * (1.2 ** num_upgrades))

    #diplay cookies per second automatic
    cps_text = font.render(f"Cookies/sec: {cookies_per_second}", True, (80,20,100))
    screen.blit(cps_text, (205, 50))

    current_time = pygame.time.get_ticks()

    if current_time - last_auto_increment >= AUTO_INCREMENT_INTERVAL:
        score += cookies_per_second
        last_auto_increment = current_time
        
    #white little effect on the cookie
    for effect in fade_effects[:]:
        # Draw the fading circle
        surface = pygame.Surface((400, 400), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(surface, (255, 255, 255, effect["alpha"]), (effect["x"], effect["y"]), effect["radius"])
        screen.blit(surface, (0, 0))

    # Update effect properties
        effect["radius"] += 2
        effect["alpha"] -= 10
        if effect["alpha"] <= 0:
            fade_effects.remove(effect)  # Remove when completely faded

    if cookie_bounce["direction"] != 0:
        cookie_bounce["scale"] += 0.05 * cookie_bounce["direction"]
    if cookie_bounce["scale"] <= 0.9:
        cookie_bounce["direction"] = 1  # Start expanding
    elif cookie_bounce["scale"] >= 1.0:
        cookie_bounce["direction"] = 0  # Stop bouncing

        # Scale the cookie image
    scaled_width = int(cookie_size[0] * cookie_bounce["scale"])
    scaled_height = int(cookie_size[1] * cookie_bounce["scale"])
    scaled_cookie = pygame.transform.scale(cookie_image, (scaled_width, scaled_height))

    # Center the cookie while it scales
    scaled_x = cookie_x + (cookie_size[0] - scaled_width) // 2
    scaled_y = cookie_y + (cookie_size[1] - scaled_height) // 2

    # Draw only the scaled cookie
    screen.blit(scaled_cookie, (scaled_x, scaled_y))

    
    #update display
    pygame.display.flip()
pygame.quit()