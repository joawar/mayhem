from precode2 import *
from config import *
from classes import Spaceship, Moving_Object, Obstacle

def game():
    screen = pygame.display.set_mode(SCREEN_RES)
    clock = pygame.time.Clock()
    player1 = Spaceship(screen, PLAYER_1_START_POS, PLAYER_1_START_VELOCITY, START_FUEL, PLAYER_1_COLOR)
    player2 = Spaceship(screen, PLAYER_2_START_POS, PLAYER_2_START_VELOCITY, START_FUEL, PLAYER_2_COLOR)
    player_list = [player1, player2]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        time_passed = clock.tick(30) # limit to 30FPS 
        time_passed_seconds = time_passed / 1000.0   # convert to seconds
        pygame.draw.rect(screen, (0,0,0), (0, 0, screen.get_width(), screen.get_height()))

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:player1.jerk(THRUST_POWER)
        if keys_pressed[pygame.K_RIGHT]:player1.rotate(ROTATIONAL_SPEED)
        if keys_pressed[pygame.K_LEFT]:player1.rotate(-ROTATIONAL_SPEED)
        if keys_pressed[pygame.K_w]:player2.jerk(THRUST_POWER)
        if keys_pressed[pygame.K_d]:player2.rotate(ROTATIONAL_SPEED)
        if keys_pressed[pygame.K_a]:player2.rotate(-ROTATIONAL_SPEED)

        for moving_object in Moving_Object.moving_object_list:
            if abs(moving_object.velocity) > CRUISING_SPEED:
                moving_object.brake()
            moving_object.accelerate()
            moving_object.move()
            moving_object.draw()
            moving_object.acceleration = GRAVITY
            moving_object.border_hit_detection()
            if type(moving_object) == Spaceship:
                print(moving_object.fuel)
                if moving_object.fuel <= 0:
                    moving_object.die()
                moving_object.burn_fuel()
            
        pygame.display.update()


if __name__ == '__main__':
    game()
    