from config import *
from classes import Spaceship, Moving_Object, Obstacle, Visible_Object, Bullet
import pygame
from pygame import Vector2

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RES)
        self.background = BACKGROUND_IMAGE.convert_alpha()
        self.clock = pygame.time.Clock()
        self.ship1 = Spaceship(PLAYER_1_START_POS, PLAYER_1_START_VELOCITY, START_FUEL, P1_CONTROLS,
                               PLAYER_1_BOOST_IMAGE, "player1")
        self.ship2 = Spaceship(PLAYER_2_START_POS, PLAYER_2_START_VELOCITY, START_FUEL, P2_CONTROLS,
                               PLAYER_2_BOOST_IMAGE, "player2")
        self.update_loop()
        
    def update_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            time_passed = self.clock.tick(30) # limit to 30FPS 
            # time_passed_seconds = time_passed / 1000.0   # convert to seconds
            self.screen.blit(self.background, (0,0))
            Visible_Object.visible_object_group.draw(self.screen)
            Moving_Object.moving_object_group.update()
            self.detect_hits()
            pygame.display.update()

    def detect_hits(self):
        """Deals with all collisions except wall collision"""
        pygame.sprite.groupcollide(Visible_Object.moving_object_group, Visible_Object.obstacle_group, True, False)
        spaceships_hit_by_bullet = pygame.sprite.groupcollide(Visible_Object.spaceship_group, Visible_Object.bullet_group, False, False)
        self.update_spaceships_health(spaceships_hit_by_bullet)
        if pygame.sprite.collide_rect(self.ship1, self.ship2):
            self.ship1.kill()
            self.ship2.kill()
    
    def update_spaceships_health(self, spaceships_hit):
        for spaceship in spaceships_hit:
            spaceship.health -= BULLET_DAMAGE
            if spaceship.health <= 0:
                spaceship.kill()

if __name__ == '__main__':
    game = Game()
    