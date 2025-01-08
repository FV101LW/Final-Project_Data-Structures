import random
import time

import pygame

# Initialize pygame
pygame.init()

# Colors (R, G, B)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (190, 200, 120) # To toggle map color
enemy_color = (255, 0, 0)  # Red for enemies
bird_color = (128, 128, 128)  # Red color for the bird

# Screen dimensions
width = 600
height = 400

# Create the screen
screen = pygame.display.set_mode((width, height))

# Title and Clock
pygame.display.set_caption('Snek')
clock = pygame.time.Clock()

# Snake settings
snake_block = 10
initial_snake_speed = 15  # Initial speed
level_up_score = 5  # Score at which to level up
max_level = 20      # Player can reach at least 20 players

# Font for the game over and score
font_style = pygame.font.Font("PressStart2P-Regular.ttf", 10)
score_font = pygame.font.Font("PressStart2P-Regular.ttf", 10)


# Function to display the score and level
def Your_score(score, level):
    value = score_font.render(f"Score: {score}  Level: {level}", True, black)
    screen.blit(value, [0, 0])

def draw_snake_head_with_eyes(x, y, snake_block):
    pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])  # Snake head
    pygame.draw.circle(screen, black, [x + snake_block // 3, y + snake_block // 3], 3)  # Left eye
    pygame.draw.circle(screen, black, [x + 2 * snake_block // 3, y + snake_block // 3], 3) # Right eye

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for i, segment in enumerate(snake_list):
        if i == 0:
            draw_snake_head_with_eyes(segment[0], segment[1], snake_block)
        else:
            pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])


# Function to draw an enemy
def draw_enemy(enemy_block, enemy_list):
    for e in enemy_list:
        pygame.draw.rect(screen, enemy_color, [e[0], e[1], enemy_block, enemy_block])

# Function to draw the bird
def draw_bird(bird_rect):
    pygame.draw.circle(screen, bird_color, bird_rect.center, 10)  
    # Simple bird represented as a circle

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 4, height / 2])


# Function to display the main menu
def main_menu():
    menu = True
    while menu:
        screen.fill(blue)
        #message("Welcome to Snake Game", green)
        font_style = pygame.font.Font('PressStart2P-Regular.ttf', 40)
        title_text = font_style.render("Snek", True, green)  # Title text
        screen.blit(title_text, [width / 2.6, height / 4])  # Center the title horizontally
        message("Press C to Play or Q to Quit", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    gameLoop()


# Function to display a cutscene
def level3_cutscene():
    screen.fill(blue)
    message("LEVEL 3: Beware!", red)
    pygame.display.update()
    time.sleep(4)  # Display message for 4 second

    screen.fill(blue)
    message("Enemies have appeared! Avoid them!", yellow)
    pygame.display.update()
    time.sleep(2)  # Show for 2 seconds

    screen.fill(blue)
    message("Get ready...", green)
    pygame.display.update()
    time.sleep(2)  # Display for 2 second

    # The cutscene is over, the game will continue
    pygame.time.wait(1000)  # A brief pause to transition smoothly into the next level

# Function to move the bird (it will move horizontally across the screen)
def move_bird(bird_rect, bird_speed):
    bird_rect.x += bird_speed
    if bird_rect.x > width:
        bird_rect.x = -50  # Reset position to the left of the screen
        bird_rect.y = random.randint(50, height - 50)  # New random vertical position
    return bird_rect

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Movement changes
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Generate food
    foodx = round(random.randrange(1, (width - snake_block) // snake_block) * snake_block)
    foody = round(random.randrange(1, (height - snake_block) // snake_block) * snake_block)

    score = 0
    level = 1
    snake_speed = initial_snake_speed

      # Start the bird off-screen to the left
    bird_rect = pygame.Rect(-50, random.randint(50, height - 50), 20, 20)  # Random vertical position
    # Bird movement speed
    bird_speed = 5

    # Initialize enemies for level 3
    enemies = []
    enemy_speed = 2  # Speed of the enemies

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            Your_score(Length_of_snake - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)

        # Draw the food
        pygame.draw.rect(screen, yellow, [foodx, foody, snake_block, snake_block])

        # Update snake position
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove last segment if snake is too long
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake collided with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Handle enemies starting from level 3
        if level >= 3:
            # Run the cutscene when entering level 3
            if score == 0:  # Ensure the cutscene only happens once when entering level 3
                level3_cutscene()

            if len(enemies) == 0:  # Generate new enemies when entering level 3
                for _ in range(3):  # Add 3 enemies
                    enemy_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                    enemy_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                    enemies.append([enemy_x, enemy_y])

            # Move enemies randomly
            for enemy in enemies:
                direction = random.choice([pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])
                if direction == pygame.K_LEFT:
                    enemy[0] -= enemy_speed
                elif direction == pygame.K_RIGHT:
                    enemy[0] += enemy_speed
                elif direction == pygame.K_UP:
                    enemy[1] -= enemy_speed
                elif direction == pygame.K_DOWN:
                    enemy[1] += enemy_speed

            # Draw the enemies
            draw_enemy(snake_block, enemies)

            # Check for collisions with enemies
            for enemy in enemies:
                if x1 == enemy[0] and y1 == enemy[1]:
                    game_close = True

        
        # If the game reaches level 5, spawn and move the bird
        if level >= 5:
            bird_x = move_bird(bird_rect, bird_speed)  # Move the bird
            draw_bird(bird_rect)  # Draw the bird

            # Check for collision with the bird
            if pygame.Rect(x1, y1, snake_block, snake_block).colliderect(bird_rect):
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, level)

        pygame.display.update()

        # Check if the snake ate the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

            # Level up when the player reaches the required score
            if score >= level * level_up_score and level < max_level:
                level += 1
                snake_speed += 5  # Increase speed with each level

        clock.tick(10) #snake_speed og

    pygame.quit()
    quit()


# Run the main menu when the game starts
main_menu()
