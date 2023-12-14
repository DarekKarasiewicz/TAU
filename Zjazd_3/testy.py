import pygame
import sys
import unittest
from main import Player, EndPoint, Barrier, Game  # Zmień "your_game_file" na rzeczywistą nazwę pliku

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game(1280, 720)

    def test_player_movement(self):
        keys = pygame.key.get_pressed()

        # Test moving up
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w)
        pygame.event.post(event)
        self.game.gracz.update_position(keys, self.game.dt, self.game.przeszkody)
        self.assertEqual(self.game.gracz.player_pos.y, 70 - 300 * self.game.dt)

        # Test moving down
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_w)
        pygame.event.post(event)
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s)
        pygame.event.post(event)
        self.game.gracz.update_position(keys, self.game.dt, self.game.przeszkody)
        self.assertEqual(self.game.gracz.player_pos.y, 70 + 300 * self.game.dt)

        # Test moving left
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_s)
        pygame.event.post(event)
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a)
        pygame.event.post(event)
        self.game.gracz.update_position(keys, self.game.dt, self.game.przeszkody)
        self.assertEqual(self.game.gracz.player_pos.x, 70 - 300 * self.game.dt)

        # Test moving right
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_a)
        pygame.event.post(event)
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)
        pygame.event.post(event)
        self.game.gracz.update_position(keys, self.game.dt, self.game.przeszkody)
        self.assertEqual(self.game.gracz.player_pos.x, 70 + 300 * self.game.dt)


    def test_collision_with_obstacle(self):
        # Create a player position that collides with an obstacle
        self.game.gracz.player_pos.topleft = (300, 200)

        # Simulate pressing the right arrow key
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)
        pygame.event.post(event)
        keys = pygame.key.get_pressed()
        self.game.gracz.update_position(keys, self.game.dt, self.game.przeszkody)

        # Check if the player position has not changed (collision occurred)
        self.assertEqual(self.game.gracz.player_pos.topleft, (300, 200))

    def test_collision_with_edge_of_screen(self):
        # Move player to the left edge of the screen
        self.game.gracz.player_pos.topleft = (0, 70)

        # Simulate pressing the left arrow key
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a)
        pygame.event.post(event)
        keys = pygame.key.get_pressed()
        self.game.gracz.update_position(keys, self.game.dt, self.game.przeszkody)

        # Check if the player position has not changed (collision occurred)
        self.assertEqual(self.game.gracz.player_pos.topleft, (0, 70))
    def test_win_condition(self):
        # Move player to the endpoint
        self.game.gracz.player_pos.topleft = (980, 580)
        
        # Use assertRaises to check if SystemExit is raised
        with self.assertRaises(SystemExit):
            self.game.check_win_condition() 
if __name__ == "__main__":
    unittest.main()