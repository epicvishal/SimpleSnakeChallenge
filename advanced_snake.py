import pygame
import random
import os
import sys  # Ensure sys is imported

# Initialize Pygame and check for errors
successes, failures = pygame.init()
print(f"Pygame initialized with {successes} success(es) and {failures} failure(s).")
if failures > 0:
    sys.exit("Critical Pygame modules failed to initialize")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Screen dimensions
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake Game")

# Fonts
font = pygame.font.SysFont("Arial", 36)
title_font = pygame.font.SysFont("Arial", 72)
small_font = pygame.font.SysFont("Arial", 24)

# Score file
SCORE_FILE = "scores.txt"


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def get_player_name():
    name = ""
    input_active = True
    while input_active:
        screen.fill(BLACK)
        draw_text("Enter Your Name:", title_font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text(name, font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
    return name


def save_score(name, score):
    with open(SCORE_FILE, "a") as f:
        f.write(f"{name}:{score}\n")


def get_high_scores():
    if not os.path.exists(SCORE_FILE):
        return []

    scores = []
    with open(SCORE_FILE, "r") as f:
        for line in f:
            name, score = line.strip().split(":")
            scores.append((int(score), name))

    scores.sort(reverse=True)
    return scores[:5]


def main_menu():
    menu = True
    selected = 0
    options = ["Start Game", "Score", "Exit Game"]

    while menu:
        screen.fill(BLACK)
        draw_text("SNAKE GAME", title_font, GREEN, screen, WIDTH // 2, HEIGHT // 4)

        for i, option in enumerate(options):
            color = WHITE if i == selected else GRAY
            draw_text(option, font, color, screen, WIDTH // 2, HEIGHT // 2 + i * 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected] == "Start Game":
                        player_name = get_player_name()
                        game_loop(player_name)
                    elif options[selected] == "Score":
                        show_high_scores()
                    elif options[selected] == "Exit Game":
                        confirm_exit()


def confirm_exit():
    confirm = True
    selected = 0
    options = ["Yes", "No"]

    while confirm:
        screen.fill(BLACK)
        draw_text("Exit Game?", title_font, RED, screen, WIDTH // 2, HEIGHT // 3)

        for i, option in enumerate(options):
            color = WHITE if i == selected else GRAY
            draw_text(option, font, color, screen, WIDTH // 2, HEIGHT // 2 + i * 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected] == "Yes":
                        pygame.quit()
                        sys.exit()
                    else:
                        confirm = False


def show_high_scores():
    scores = get_high_scores()
    viewing = True

    while viewing:
        screen.fill(BLACK)
        draw_text("High Scores", title_font, GREEN, screen, WIDTH // 2, HEIGHT // 4)

        if not scores:
            draw_text("No scores yet!", font, WHITE, screen, WIDTH // 2, HEIGHT // 2)
        else:
            for i, (score, name) in enumerate(scores):
                draw_text(f"{i + 1}. {name}: {score}", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + i * 40)

        draw_text("Press any key to return", small_font, GRAY, screen, WIDTH // 2, HEIGHT - 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                viewing = False


def game_loop(player_name):
    snake = [(WIDTH // 2, HEIGHT // 2)]
    snake_dir = (CELL_SIZE, 0)
    food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    lives = 3
    score = 0
    running = True

    def reset_snake():
        nonlocal snake, snake_dir
        snake = [(WIDTH // 2, HEIGHT // 2)]
        snake_dir = (CELL_SIZE, 0)

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                    snake_dir = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                    snake_dir = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                    snake_dir = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                    snake_dir = (CELL_SIZE, 0)

        # Snake movement
        new_head = (
            (snake[0][0] + snake_dir[0]) % WIDTH,
            (snake[0][1] + snake_dir[1]) % HEIGHT
        )
        snake.insert(0, new_head)

        # Food collision
        if snake[0] == food:
            score += 1
            food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        else:
            snake.pop()

        # Collision check
        if snake[0] in snake[1:]:
            lives -= 1
            if lives > 0:
                reset_snake()
            else:
                running = False

        # Draw elements
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

        # Display info
        draw_text(f"Score: {score}", font, WHITE, screen, 100, 20)
        draw_text(f"Lives: {lives}", font, WHITE, screen, WIDTH - 100, 20)

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(10)

    # Game over sequence
    save_score(player_name, score)
    screen.fill(BLACK)
    draw_text(f"Final Score: {score}", title_font, WHITE, screen, WIDTH // 2, HEIGHT // 2)
    draw_text("Returning to main menu...", small_font, GRAY, screen, WIDTH // 2, HEIGHT - 50)
    pygame.display.flip()
    pygame.time.wait(2000)


if __name__ == "__main__":
    main_menu()
    pygame.quit()  # Added final cleanup