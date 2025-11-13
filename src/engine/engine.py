import pygame

# This will be the main 2D game engine module
class GameEngine:
    def __init__(self, width=800, height=600, title="2D Game Engine"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()