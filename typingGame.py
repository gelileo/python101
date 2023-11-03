import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
WORD_SPEED = 1  # Adjust the speed as desired (1 word per second)
WORD_GEN_EVENT = pygame.USEREVENT + 1
WORD_REMOVE_EVENT = pygame.USEREVENT + 2
WORD_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")

# Load fonts
font = pygame.font.Font(None, FONT_SIZE)

# List of words to type
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango"]
current_word = random.choice(word_list)

# Word position and speed
word_x = random.randint(10, WIDTH - FONT_SIZE * len(current_word))
word_y = 10
word_speed = 0  # Start with a speed of 0

# Game variables
score = 0
game_over = False
remove_word_flag = False  # Flag to determine when to remove a word

def generate_word():
    global current_word, word_x, word_y, word_speed, remove_word_flag
    current_word = random.choice(word_list)
    word_x = random.randint(10, WIDTH - FONT_SIZE * len(current_word))
    word_y = 10
    word_speed = WORD_SPEED
    remove_word_flag = False

def remove_word():
    global score, current_word, remove_word_flag
    if not remove_word_flag:
        score += 1
    remove_word_flag = True

# Create events for generating and removing words
pygame.time.set_timer(WORD_GEN_EVENT, 2000)
pygame.time.set_timer(WORD_REMOVE_EVENT, 10000)

clock = pygame.time.Clock()  # Create a clock object to control the frame rate

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == WORD_GEN_EVENT:
            generate_word()
        if event.type == WORD_REMOVE_EVENT:
            remove_word()

    keys = pygame.key.get_pressed()

    # Handle typing
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.unicode == current_word[0]:
            current_word = current_word[1:]
            if len(current_word) == 0:
                remove_word()

    screen.fill(BACKGROUND_COLOR)
    
    # Display the current word
    text = font.render(current_word, True, WORD_COLOR)
    screen.blit(text, (word_x, word_y))
    
    # Display the score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    word_y += word_speed

    # Limit the frame rate to control the word drop speed
    clock.tick(60)  # Adjust the frame rate as needed

    if word_y > HEIGHT:
        generate_word()

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
