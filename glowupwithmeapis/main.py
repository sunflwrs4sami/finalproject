import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glow Up App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, text, position, size=(200, 50), inactive_color=GRAY, active_color=GREEN):
        self.text = text
        self.font = font
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.rect = pygame.Rect(position, size)
        self.is_hovered = False

    def draw(self, screen):
        color = self.active_color if self.is_hovered else self.inactive_color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)  # Rounded corners
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

def intro_screen():
    intro_font = pygame.font.Font(None, 50)
    intro_text = intro_font.render("Welcome to Glow Up App", True, BLACK)
    intro_rect = intro_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    start_button = Button("Start", (WIDTH // 2, HEIGHT * 3 // 4))

    screen.fill(WHITE)
    screen.blit(intro_text, intro_rect)
    start_button.draw(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    return

def instruction_screen():
    instruction_font = pygame.font.Font(None, 36)
    instruction_text = [
        "Instructions:",
        "- Click on the 'Next' button to proceed to the options.",
        "- Explore Fitness, Beauty, and Motivational Quotes!",
        "- Press 'Esc' at any time to exit the app."
    ]
    instruction_rects = []

    screen.fill(WHITE)
    for i, text in enumerate(instruction_text):
        text_surface = instruction_font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4 + i * 50))
        screen.blit(text_surface, text_rect)
        instruction_rects.append(text_rect)

    next_button = Button("Next", (WIDTH // 2, HEIGHT * 3 // 4))
    next_button.draw(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.rect.collidepoint(event.pos):
                    return

def option_screen():
    screen.fill(WHITE)
    options = ["Fitness", "Beauty", "Motivational Quotes"]
    buttons = []

    for i, option in enumerate(options):
        button = Button(option, (WIDTH // 2, HEIGHT // 4 + i * 75))
        buttons.append(button)

    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        for button in buttons:
            button.update(mouse_pos)
            button.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        print(f"Clicked: {button.text}")
                        tips_screen(button.text)

def tips_screen(option):
    screen.fill(WHITE)
    # Fetch tips based on the selected option
    if option == "Fitness":
        tips = ["Tip 1: Fitness tip 1", "Tip 2: Fitness tip 2", "Tip 3: Fitness tip 3"]
    elif option == "Beauty":
        tips = ["Tip 1: Skincare tip 1", "Tip 2: Skincare tip 2", "Tip 3: Makeup tip 1"]
    elif option == "Motivational Quotes":
        tips = ["Quote 1", "Quote 2", "Quote 3"]
    else:
        tips = []

    # Display tips
    y_offset = HEIGHT // 4
    for tip in tips:
        text_surface = font.render(tip, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 50

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

def main():
    intro_screen()
    instruction_screen()
    option_screen()

if __name__ == "__main__":
    main()
