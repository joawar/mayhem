# import pygame
# from precode2 import Vector2D

# screen_res = (640,480)
# pygame.init()
# screen = pygame.display.set_mode(screen_res)
# clock = pygame.time.Clock()
# ANGLE = 20
# pos = Vector2D(300, 240)
# velocity = Vector2D(2, -3)
# COLOR = (200,0,0)
# COLOR2 = (0, 200, 0)
# LENGTH = 40
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

#     pygame.draw.rect(screen, (0,0,0), (0, 0, screen.get_width(), screen.get_height()))
#     time_passed = clock.tick(30) # limit to 30FPS 
#     time_passed_seconds = time_passed / 1000.0   # convert to seconds
#     point1 = pos
#     point2 = point1 + (velocity.normalized().rotate(180 + ANGLE))*LENGTH
#     point3 = point1+velocity.normalized().rotate(180 - ANGLE)*LENGTH
#     ball = pygame.draw.polygon(screen, COLOR, [[point1.x, point1.y], [point2.x, point2.y], [point3.x, point3.y]])
#     ball = pygame.draw.circle(screen, COLOR2, [pos.x, pos.y], 5)
#     pos += velocity
#     pygame.display.update()


class A:
    name = "alfa"
etelleranna= A()

print(etelleranna.name)