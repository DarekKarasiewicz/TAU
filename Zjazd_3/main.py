import pygame
import sys

class Player:
    def __init__(self, screen):
        self.player_pos = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2, 30, 30)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def update_position(self, keys, dt, przeszkody):
        new_pos = self.player_pos.copy()

        if keys[pygame.K_w]:
            new_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            new_pos.y += 300 * dt
        if keys[pygame.K_a]:
            new_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            new_pos.x += 300 * dt

        # Sprawdzamy kolizję z przeszkodami
        for przeszkoda in przeszkody:
            if new_pos.colliderect(przeszkoda.rect):
                return

        # Ograniczamy ruch gracza do granic planszy
        new_pos.x = max(0, min(new_pos.x, self.screen_width - new_pos.width))
        new_pos.y = max(0, min(new_pos.y, self.screen_height - new_pos.height))

        self.player_pos = new_pos

class EndPoint:
    def __init__(self, screen, x, y, radius):
        self.end_point_pos = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (int(self.end_point_pos.x), int(self.end_point_pos.y)), self.radius)

    def check_collision(self, player_pos):
        distance = pygame.Vector2(player_pos.center).distance_to(self.end_point_pos)
        return distance < self.radius

class Barrier:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, "gray", self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.gracz = Player(self.screen)
        self.punkt_koncowy = EndPoint(self.screen, 1000, 100, 20)
        self.przeszkody = [
            Barrier(300, 200, 50, 50),
            Barrier(500, 400, 100, 30),
            Barrier(800, 300, 60, 80)
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw_objects(self):
        self.screen.fill("blue")
        self.punkt_koncowy.draw(self.screen)
        pygame.draw.rect(self.screen, "red", self.gracz.player_pos)

        for przeszkoda in self.przeszkody:
            przeszkoda.draw(self.screen)

    def check_win_condition(self):
        if self.punkt_koncowy.check_collision(self.gracz.player_pos):
            print("WIN")
            pygame.quit()
            sys.exit()

    def run(self):
        while self.running:
            self.handle_events()

            keys = pygame.key.get_pressed()
            self.gracz.update_position(keys, self.dt, self.przeszkody)

            self.draw_objects()

            self.check_win_condition()

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()