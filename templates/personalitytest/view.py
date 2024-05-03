import pygame
import os

class PersonalityTest:
    def __init__(self):
        self.questions = [
            "You prefer to spend your free time:",
            "When making decisions, you rely more on:",
            "You consider yourself to be more:",
            "In social situations, you tend to be:",
            "You are more comfortable with:",
            "You value:",
            "You prefer to work in a:",
            "You see yourself as:",
            "Your favorite type of weather is:",
            "Your ideal vacation destination is:",
            "Your preferred mode of transportation is:",
            "You feel most energized when:",
            "Your favorite type of music is:",
            "Your ideal way to relax is:",
            "You enjoy hobbies that involve:"
        ]
        self.options = [
            ["Reading a book", "Going for a hike", "Watching movies"],
            ["Logic and reason", "Intuition and gut feeling", "Seeking advice from others"],
            ["Introverted and reflective", "Outgoing and sociable", "Balanced and adaptable"],
            ["Observant and reserved", "Talkative and enthusiastic", "Diplomatic and empathetic"],
            ["Routine and structure", "Spontaneity and change", "Finding a middle ground"],
            ["Knowledge and intelligence", "Creativity and imagination", "Harmony and peace"],
            ["Quiet and organized environment", "Dynamic and collaborative workspace", "Flexible and adaptable setting"],
            ["Practical and analytical", "Dreamy and visionary", "Compassionate and understanding"],
            ["Sunny and warm", "Rainy and cozy", "Snowy and magical"],
            ["Historical cities and landmarks", "Tropical beaches and islands", "Countryside and nature retreats"],
            ["Car", "Bicycle", "Train"],
            ["Planning and organizing events", "Exploring new ideas and possibilities", "Helping others and making a difference"],
            ["Classical and instrumental", "Pop and upbeat", "Indie and alternative"],
            ["Meditating or practicing yoga", "Going for a run or exercise", "Spending time with friends and family"],
            ["Solving puzzles and brain teasers", "Creating art or crafting", "Cooking or baking"]
        ]

    def get_questions(self):
        return self.questions

    def get_options(self):
        return self.options

    def get_cake_type(self, answers):
        # Count the number of times each option (A, B, C) appears in the answers
        option_counts = {'A': 0, 'B': 0, 'C': 0}
        for answer in answers:
            option_counts[answer] += 1

        # Determine the cake type based on the option counts
        if option_counts['A'] >= 2:
            return "Chocolate Cake"
        elif option_counts['B'] >= 2:
            return "Red Velvet Cake"
        elif option_counts['C'] >= 2:
            return "Vanilla Cake"
        else:
            return "Carrot Cake"

    def get_cake_description(self, cake_type):
        descriptions = {
            "Vanilla Cake": "You are a Vanilla Cake! Just like this classic cake, you are simple yet elegant. You appreciate the little things in life and enjoy spending time with loved ones.",
            "Chocolate Cake": "You are a Chocolate Cake! Your rich and indulgent personality makes you irresistible to those around you. You have a deep passion for life and love to indulge in your favorite activities.",
            "Red Velvet Cake": "You are a Red Velvet Cake! Your vibrant personality and charm light up any room. You are bold and adventurous, always ready for new experiences.",
            "Carrot Cake": "You are a Carrot Cake! Just like this unique cake, you are full of surprises. Your warmth and kindness shine through, and you have a knack for bringing joy to others."
        }
        return descriptions.get(cake_type, "Your personality is as unique as a custom-made cake! Unfortunately, we don't have a description for your result.")

class PersonalityTestView:
    def __init__(self, screen, model):
        self.screen = screen
        self.model = model
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.answers = []
        self.current_question_index = 0
        self.state = "INTRO"  # Initial state

        # Get the current working directory
        current_directory = os.path.dirname(__file__)

        # Construct the full path to the image file
        self.image_path = os.path.join(current_directory, 'cake_image.png')

        # Load the image
        self.cake_image = pygame.image.load(self.image_path)

    def run_test(self):
        while True:
            if self.state == "INTRO":
                self.draw_intro()
            elif self.state == "INSTRUCTIONS":
                self.draw_instructions()
            elif self.state == "TEST":
                self.draw_test()
            elif self.state == "RESULTS":
                self.draw_results()
            else:
                break  # Exit the loop

            pygame.display.flip()
            self.clock.tick(30)

    def draw_intro(self):
        self.screen.fill((255, 255, 255))

        # Display cake image
        self.screen.blit(self.cake_image, (270, 100))

        title_text = self.font.render("Welcome to Cake Personality Test!", True, (0, 0, 0))
        self.screen.blit(title_text, (200, 300))

        start_button = pygame.Rect(300, 400, 200, 50)
        pygame.draw.rect(self.screen, (255, 182, 193), start_button)  # Light pink button color
        start_text = self.font.render("Start Test", True, (0, 0, 0))
        self.screen.blit(start_text, (320, 410))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    self.state = "INSTRUCTIONS"

    def draw_instructions(self):
        self.screen.fill((255, 255, 255))
        instruction_text = [
            "Instructions:",
            "- Answer each question honestly.",
            "- Press A, B, or C to select your answer.",
            "- Once you finish, press Continue to see your result."
        ]
        y_offset = 50
        for text in instruction_text:
            text_surface = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 40

        continue_button = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(self.screen, (255, 182, 193), continue_button)  # Light pink button color
        continue_text = self.font.render("Continue", True, (0, 0, 0))
        self.screen.blit(continue_text, (320, 310))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if continue_button.collidepoint(mouse_pos):
                    self.state = "TEST"
                    self.current_question_index = 0

    def draw_test(self):
        while self.current_question_index < len(self.model.get_questions()):
            question = self.model.get_questions()[self.current_question_index]
            options = self.model.get_options()[self.current_question_index]
            self.draw_question(question, options)
            pygame.display.flip()
            self.clock.tick(30)

        # Once all questions are answered, display result
        cake_type = self.model.get_cake_type(self.answers)
        self.cake_description = self.model.get_cake_description(cake_type)
        self.state = "RESULTS"

    def draw_question(self, question, options):
        self.screen.fill((255, 255, 255))
        question_text = self.font.render(question, True, (0, 0, 0))
        self.screen.blit(question_text, (50, 50))

        # Display options as buttons
        option_buttons = []
        for i, option in enumerate(options):
            button = pygame.Rect(50, 150 + 70 * i, 700, 50)  # Adjust button position and size as needed
            option_buttons.append(button)
            pygame.draw.rect(self.screen, (255, 182, 193), button)  # Light pink button color
            option_text = self.font.render(option, True, (0, 0, 0))
            self.screen.blit(option_text, (button.x + 10, button.y + 10))

        pygame.display.update()

        # Handle button clicks
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, button in enumerate(option_buttons):
                    if button.collidepoint(mouse_pos):
                        # Record the chosen option
                        self.answers.append(chr(ord('A') + i))  # Convert index to option letter
                        self.next_question()

    def next_question(self):
        self.current_question_index += 1

    def draw_results(self):
        self.screen.fill((255, 255, 255))
        result_text = self.font.render("Your cake type is:", True, (0, 0, 0))
        self.screen.blit(result_text, (50, 50))
        cake_type_text = self.font.render(self.model.get_cake_type(self.answers), True, (255, 0, 0))
        self.screen.blit(cake_type_text, (50, 100))
        description_text = self.font.render(self.cake_description, True, (0, 0, 0))
        self.screen.blit(description_text, (50, 150))

        pygame.display.update()

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cake Personality Test")

# Create an instance of the PersonalityTest class
test = PersonalityTest()

# Create an instance of the PersonalityTestView class
view = PersonalityTestView(screen, test)

# Run the test
view.run_test()

# Quit pygame
pygame.quit()
