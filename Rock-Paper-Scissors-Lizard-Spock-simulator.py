import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# Count of elements
count_of_elements = 30

# Set the window caption
pygame.display.set_caption("Rock-Paper-Scissors-Lizard-Spock Simulator")

# Load the images for rock, paper, scissors, lizard, and spock
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")
lizard_img = pygame.image.load("lizard.png")
spock_img = pygame.image.load("spock.png")

# Resize the images to 50x50 pixels
img_size = 50
small_img_size = 20  # Small image size for count indicator
rock_img = pygame.transform.scale(rock_img, (img_size, img_size))
paper_img = pygame.transform.scale(paper_img, (img_size, img_size))
scissors_img = pygame.transform.scale(scissors_img, (img_size, img_size))
lizard_img = pygame.transform.scale(lizard_img, (img_size, img_size))
spock_img = pygame.transform.scale(spock_img, (img_size, img_size))

# Smaller images for count indicators
small_rock_img = pygame.transform.scale(rock_img, (small_img_size, small_img_size))
small_paper_img = pygame.transform.scale(paper_img, (small_img_size, small_img_size))
small_scissors_img = pygame.transform.scale(scissors_img, (small_img_size, small_img_size))
small_lizard_img = pygame.transform.scale(lizard_img, (small_img_size, small_img_size))
small_spock_img = pygame.transform.scale(spock_img, (small_img_size, small_img_size))

# Define the GameObject class to represent each object (rock, paper, scissors, lizard, spock)
class GameObject:
    def __init__(self, x, y, image, strength):
        self.x = x
        self.y = y
        self.image = image
        self.strength = strength
        self.target_object = None
        self.move_direction = (random.randint(-100, 100), random.randint(-100, 100))
        self.move_direction = self.normalize_vector(self.move_direction)

    def normalize_vector(self, vector):
        magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        if magnitude == 0:
            return vector
        return (vector[0] / magnitude, vector[1] / magnitude)

    def move_randomly(self):
        move_speed = 3
        self.x += self.move_direction[0] * move_speed
        self.y += self.move_direction[1] * move_speed

        # Check if the object reached the end of the screen, then choose a new random direction
        if self.x <= 0 or self.x >= screen_width - img_size:
            self.move_direction = (-self.move_direction[0], self.move_direction[1])
        if self.y <= 0 or self.y >= screen_height - img_size:
            self.move_direction = (self.move_direction[0], -self.move_direction[1])

        self.move_direction = self.normalize_vector(self.move_direction)

    def find_nearest_object(self, objects):
        nearest_distance = float('inf')
        nearest_obj = None

        for obj in objects:
            if obj is not self:
                distance = math.sqrt((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_obj = obj

        return nearest_obj

    def update_target(self, objects):
        self.target_object = self.find_nearest_object(objects)

# Create a list to hold all the game objects (rocks, papers, scissors, lizards, spocks)
game_objects = []

# Create 30 rock objects and add them to the list
for _ in range(count_of_elements):
    x = random.randint(0, screen_width - img_size)
    y = random.randint(0, screen_height - img_size)
    rock = GameObject(x, y, rock_img, 1)  # Rock crushes Scissors (strength = 1)
    game_objects.append(rock)

# Create 30 paper objects and add them to the list
for _ in range(count_of_elements):
    x = random.randint(0, screen_width - img_size)
    y = random.randint(0, screen_height - img_size)
    paper = GameObject(x, y, paper_img, 3)  # Paper covers Rock (strength = 3)
    game_objects.append(paper)

# Create 30 scissors objects and add them to the list
for _ in range(count_of_elements):
    x = random.randint(0, screen_width - img_size)
    y = random.randint(0, screen_height - img_size)
    scissors = GameObject(x, y, scissors_img, 2)  # Scissors cuts Paper (strength = 2)
    game_objects.append(scissors)

# Create 30 lizard objects and add them to the list
for _ in range(count_of_elements):
    x = random.randint(0, screen_width - img_size)
    y = random.randint(0, screen_height - img_size)
    lizard = GameObject(x, y, lizard_img, 5)  # Lizard poisons Spock (strength = 5)
    game_objects.append(lizard)

# Create 30 spock objects and add them to the list
for _ in range(count_of_elements):
    x = random.randint(0, screen_width - img_size)
    y = random.randint(0, screen_height - img_size)
    spock = GameObject(x, y, spock_img, 4)  # Spock vaporizes Rock (strength = 4)
    game_objects.append(spock)

# Create a game loop to keep the screen open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the target for each game object to the nearest one
    for obj in game_objects:
        obj.update_target(game_objects)

    # Move all the game objects randomly
    for obj in game_objects:
        obj.move_randomly()

    # Handle collisions and transformations
    for obj in game_objects:
        for other_obj in game_objects:
            if obj is not other_obj and pygame.Rect(obj.x, obj.y, img_size, img_size).colliderect(
                    pygame.Rect(other_obj.x, other_obj.y, img_size, img_size)):
                # Handle rock-paper-scissors-lizard-spock interactions
                if (obj.strength == 1 and other_obj.strength == 2) or (obj.strength == 2 and other_obj.strength == 3) \
                        or (obj.strength == 3 and other_obj.strength == 1) or (obj.strength == 4 and other_obj.strength == 1) \
                        or (obj.strength == 5 and other_obj.strength == 4) or (obj.strength == 2 and other_obj.strength == 5) \
                        or (obj.strength == 4 and other_obj.strength == 2) or (obj.strength == 3 and other_obj.strength == 4) \
                        or (obj.strength == 5 and other_obj.strength == 3) or (obj.strength == 1 and other_obj.strength == 5):
                    other_obj.image = obj.image
                    other_obj.strength = obj.strength

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Count the number of each element
    rock_count = sum(1 for obj in game_objects if obj.strength == 1)
    paper_count = sum(1 for obj in game_objects if obj.strength == 3)
    scissors_count = sum(1 for obj in game_objects if obj.strength == 2)
    lizard_count = sum(1 for obj in game_objects if obj.strength == 5)
    spock_count = sum(1 for obj in game_objects if obj.strength == 4)

    # Draw the count indicators on the screen
    screen.blit(small_rock_img, (10, 10))
    screen.blit(small_paper_img, (10, 40))
    screen.blit(small_scissors_img, (10, 70))
    screen.blit(small_lizard_img, (10, 100))
    screen.blit(small_spock_img, (10, 130))

    font = pygame.font.SysFont(None, 30)
    rock_text = font.render(f": {rock_count}", True, (0, 0, 0))
    paper_text = font.render(f": {paper_count}", True, (0, 0, 0))
    scissors_text = font.render(f": {scissors_count}", True, (0, 0, 0))
    lizard_text = font.render(f": {lizard_count}", True, (0, 0, 0))
    spock_text = font.render(f": {spock_count}", True, (0, 0, 0))

    screen.blit(rock_text, (35, 10))
    screen.blit(paper_text, (35, 40))
    screen.blit(scissors_text, (35, 70))
    screen.blit(lizard_text, (35, 100))
    screen.blit(spock_text, (35, 130))

    # Draw all the game objects on the screen
    for obj in game_objects:
        screen.blit(obj.image, (obj.x, obj.y))

    # Update the display
    pygame.display.update()

    # Add a small delay to control the speed of movement
    pygame.time.delay(30)

# Quit Pygame properly
pygame.quit()
