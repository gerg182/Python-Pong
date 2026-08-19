import pygame
import random

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

Lost = False
Lost_player1 = False
Lost_player2 = False
player_score = 0

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
        self.x_list = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        self.y_list = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        self.x_pick = random.choice(self.x_list)
        self.y_pick = random.choice(self.y_list)

    def spawn(self):
        pygame.draw.rect(display_surf, white, (self.pos_y, self.pos_x, 5, 5))

    def move(self):
        self.pos_x += self.x_pick * 1.5
        self.pos_y += self.y_pick * 1.5

    def bounce(self):
        global Lost_player1
        global Lost_player2
        global Lost
        if self.pos_x <= 0 or self.pos_x >= DISPLAY_HEIGHT:
            self.x_pick = self.x_pick * -1
        
        if self.pos_y <= 0:
            Lost_player1 = True
            Lost = True
        elif self.pos_y >= DISPLAY_WIDTH:
            Lost_player2 = True
            Lost = True

paddle_game = paddle(1,200,1,400,pygame.K_w,pygame.K_s)
paddle_game_2 = paddle(798,200,798,400,pygame.K_UP,pygame.K_DOWN)
ball_game = ball(300, 400, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    ball_game.move()
    ball_game.bounce()

    paddle_game.move(keys,paddle_speed)
    paddle_game_2.move(keys,paddle_speed)

    display_surf.fill(black)
    paddle_game.draw()
    paddle_game_2.draw()
    ball_game.spawn()

    if Lost == True:
        overlay = pygame.Surface((display_surf.get_width(), display_surf.get_height()))
        overlay.set_alpha(180)
        overlay.fill((30, 30, 30))
        display_surf.blit(overlay, (0, 0))
        if keys[pygame.K_r]:
            new_game()

        font = pygame.font.Font(None, 74)
        if Lost_player1 == True:
            text_surface = font.render(f"Player 1 lost\nPress R to restart", True, (255, 255, 255))
        elif Lost_player2:
            text_surface = font.render(f"Player 2 lost\nPress R to restart", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(display_surf.get_width() // 2, display_surf.get_height() // 2))
        display_surf.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit