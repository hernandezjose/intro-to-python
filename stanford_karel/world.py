import pygame
from pygame.locals import MOUSEBUTTONDOWN

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
L_GREY = (158, 158, 158)
D_GREY = (56, 56, 56)
GREEN = (91, 153, 0)
RED = (240, 0, 0)
L_BLUE = (0, 124, 150)
D_BLUE = (34, 25, 117)
YELLOW = (255, 236, 0)
CLR = (1, 1, 1)
ORANGE = (255, 165, 0)
PINK = (255, 165, 245)
TEAL = (0, 160, 180)
PURPLE = (200, 0, 255)


IDEAL_HEIGHT = 600
IDEAL_WIDTH = 800


def wait_for_click():
    pygame.mouse.set_visible(True)
    while True:
        for event in pygame.event.get():
            print(f"Received event {event}")
            if event.type == MOUSEBUTTONDOWN:
                print(f"Successfully heard MOUSEBUTTONDOWN")
                return


class KarelWorld(object):

    HEIGHT = 600
    WIDTH = 800

    def __init__(
            self,
            rows: int,
            cols: int
    ):
        self._rows = rows
        self._cols = cols
        self._tile_width = min(self.WIDTH / (self._cols + 2), self.HEIGHT / (self._rows + 2))
        # variables for later
        self._background = None

    def build_background(self):
        if self._background:
            return self._background
        # create the background
        self._background = pygame.Surface(size=(self.WIDTH, self.HEIGHT))
        self._background.fill(color=WHITE)
        #
        return self._background

    def render(self):
        pygame.init()
        pygame.display.set_mode(size=(self.WIDTH, self.HEIGHT))
        # draw karel
        self.build_background()
        # run karel
        # close out the screen
        wait_for_click()
        pygame.quit()


if __name__ == "__main__":
    world = KarelWorld()
    world.render()
