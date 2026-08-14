import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
display_surf = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
display_surf.fill((0,0,0))
pygame.display.set_caption("My PyGame Window")

#Colors
white = (255, 255, 255)
black = (0, 0, 0)

paddle_speed = 6
clock = pygame.time.Clock()

class paddle:
    def __init__(self, pos_x, pos_y, pos_x_end, pos_y_end, up_key, down_key):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_end = pos_x_end
        self.pos_y_end = pos_y_end
        self.up_key = up_key
        self.down_key = down_key

    def move(self,keys,paddle_speed):
        if keys[self.up_key] and self.pos_y > 0:
            self.pos_y -= paddle_speed
            self.pos_y_end -= paddle_speed
        if keys[self.down_key] and self.pos_y_end < DISPLAY_HEIGHT:
            self.pos_y += paddle_speed
            self.pos_y_end += paddle_speed

    def draw(self):
        pygame.draw.line(display_surf, white, (self.pos_x, self.pos_y), (self.pos_x_end, self.pos_y_end), 5)

class ball:
    def __init__(self, pos_x, pos_y, radius):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius

    def spawn(self):
        pygame.draw.circle(display_surf, white, (self.pos_x, self.pos_y), self.radius)

paddle_game = paddle(1,200,1,400,pygame.K_w,pygame.K_s)
paddle_game_2 = paddle(798,200,798,400,pygame.K_UP,pygame.K_DOWN)
ball_game = ball(400, 300, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    paddle_game.move(keys,paddle_speed)
    paddle_game_2.move(keys,paddle_speed)

    display_surf.fill(black)
    paddle_game.draw()
    paddle_game_2.draw()
    ball_game.spawn()

    pygame.display.flip()
    clock.tick(60)

pygame.quit