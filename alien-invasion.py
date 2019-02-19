import sys
import pygame
from settings import Settings
def run_game():
#初始化
    pygame.init()
    ai_seetings=Settings()
    screen=pygame.display.set_mode((ai_seetings.screen_width,ai_seetings.screnn_heght))
    pygame.display.set_caption("Alien Invasion")
    #开始主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_seetings.bg_color)
        pygame.display.flip()
run_game()
