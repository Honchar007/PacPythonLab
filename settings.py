from pygame.math import Vector2 as vec
# screen settings
TOP_BOTTOM_BUFFER = 50
WIDTH, HEIGHT = 610, 670
FPS = 60
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

# color settings
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR = (190, 194, 15)

# font settings
START_FONT = 'arial black'
START_TEXT_SIZE = 16
# player settings
PLAYER_START_POS = vec(1,1)

# mob settings
