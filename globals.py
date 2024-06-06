HIGH_SCORE = 4
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
X_AXIS = WINDOW_WIDTH // 2
Y_AXIS = WINDOW_HEIGHT // 2
COLORS = ("blue", "green", "yellow", "aquamarine", "orange", "purple", "pink")
MOVE_DISTANCE = 20
STARTING_POSITION = (0, 0)
SNAKE_LENGTH = 4

# Notice that no matter changes made to this option, enemy snake will always behave like it is set to 0.
# CHANGE BORDER MODE:
# 0 -> SNAKE LOOPS AROUND THE BOARD WARNING!!! BUGGY CORNERS
# 1 -> SNAKE DIES WHEN COLLIDING WITH A WALL
BORDER_MODE = 1

# Notice enemy snake never eats its own tail - thanks to that it is a bit more dangerous.
# CHANGE TAIL MODE:
# 0 -> SNAKE EATS ITS TAIL ON COLLISION
# 1 -> SNAKE DIES WHEN COLLIDING WITH ITS TAIL
TAIL_MODE = 0
