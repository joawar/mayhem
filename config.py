from vector import Vector2
import pygame

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT)

RED = (255, 0, 0)
BLUE = (0, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)

SPACESHIP_ANGLE = 20
SPACESHIP_SIZE = 40

PLAYER_1_START_POS = Vector2(610, 250)
PLAYER_2_START_POS = Vector2(30, 30)

BACKGROUND_IMAGE_FNAME = "images/background.jpg"
PLAYER_1_BOOST_IMAGE_FNAME = "images/player1_boost.png"
PLAYER_2_BOOST_IMAGE_FNAME = "images/player2_boost.png"
PLAYER_1_BOOST_IMAGE = pygame.image.load(PLAYER_1_BOOST_IMAGE_FNAME)
PLAYER_2_BOOST_IMAGE = pygame.image.load(PLAYER_2_BOOST_IMAGE_FNAME)
BACKGROUND_IMAGE = pygame.image.load(BACKGROUND_IMAGE_FNAME)
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, SCREEN_RES)

PLAYER_1_START_VELOCITY = Vector2(0,-1) # can't have (0,0) because it will give an error when trying to normalize
PLAYER_2_START_VELOCITY = Vector2(0,-1)

START_FUEL = 100000000
FUEL_CONSUMPTION = 10

THRUST_STRENGTH = 0.5
ANGULAR_SPEED = 6

GRAVITY = Vector2(0, 0.1)

MAX_SPEED = 10
CRUISING_SPEED = 6

REVERSE_STRENGTH = 1

BULLET_SPEED = 15
BULLET_RADIUS = 2

RESPAWN_TIME = 1 # seconds

P1_CONTROLS = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]
P2_CONTROLS = [pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s]