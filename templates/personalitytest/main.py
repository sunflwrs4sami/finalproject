import pygame
from view import PersonalityTestView
from model import PersonalityTest

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cake Personality Test")

    model = PersonalityTest()
    view = PersonalityTestView(screen, model)
    view.run_test()

    pygame.quit()

if __name__ == "__main__":
    main()

