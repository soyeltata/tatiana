from tatiana import World, Entity
from movement import MovementSystem
from os.path import abspath

RESX = 800
RESY = 600
SPRITE = 'image.png'

player = Entity('mainobj', (0, 0), abspath(SPRITE))

w = World(RESX, RESY)
w.add_entity(player)
w.add_system('movement', MovementSystem)
w.set_target_fps(30)
w.run()
