import pygame

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
#初始化
    pygame.init()
    ai_seetings = Settings()
    screen = pygame.display.set_mode((ai_seetings.screen_width, ai_seetings.screnn_heght))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    #开始主循环
    while True:
        gf.check_events()

        screen.fill(ai_seetings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()
