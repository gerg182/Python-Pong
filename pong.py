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


class paddle:
    def __init__(self, pos_x, pos_y, pos_x_end, pos_y_end):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_end = pos_x_end
        self.pos_y_end = pos_y_end

    def move(self):
        

    def draw(self):
        pygame.draw.line(display_surf, white, (self.pos_x, self.pos_y), (self.pos_x_end, self.pos_y_end), 5)

paddle_game = paddle(1,200,1,400)
paddle_game_2 = paddle(798,200,798,400)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    paddle_game.draw()
    paddle_game_2.draw()

    pygame.display.flip()

pygame.quit