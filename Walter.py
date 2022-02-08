from unicodedata import name
import pygame
import os


class Settings(object):
    spaceship_size = (60, 60)
    Background = (1060, 690)
    window_height = 690
    window_width = 1060
    path_file = os.path.dirname(os.path.abspath(__file__))
    path_image = os.path.join(path_file, "images")
    path_sound = os.path.join(path_file, "sound")
    title = "Spaceship"


class Background(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.path_image, filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Settings.window_width, Settings.window_height))
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.path_image, filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image, Settings.spaceship_size)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left = (Settings.window_width // 2) - self.rect.width // 2
        self.rect.top = (Settings.window_height // 2) - self.rect.height // 2
        self.spaceship = pygame.transform.rotate(self.image, 22.5)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)



class Game(object):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
        pygame.display.set_caption(Settings.title)
        self.clock = pygame.time.Clock()
        self.background = Background("Background.jpg")
        self.spaceship = Spaceship("spaceship.png")
        self.name = pygame.sprite.Group()
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.watch_for_events()
            self.draw()
            self.update()

        pygame.quit()

    def watch_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_p:
                    self.pause = not self.pause

                if event.key == pygame.K_k:
                    self.spaceship.rotate_l()
                if event.key == pygame.K_l:
                    self.spaceship.rotate_r()

    def update(self):
        self.name.update()
        self.name.update()

    def draw(self):
        self.background.draw(self.screen)
        self.spaceship.draw(self.screen)
        self.name.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    os.environ["SDL_VIDEO_WINDOW_POS"] = "170, 50"

    game = Game()
    game.run()
