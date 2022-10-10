from engine import World, Entity
from engine.components import SpriteComponent
from movement import MovementSystem
from os.path import abspath

player = Entity('mainobj', (0, 0), abspath('assets/main.png'))

sc = player.get_component(SpriteComponent)
sc.add_image(abspath('assets/main2.png'), True)
sc.scalingX, sc.scalingY = 4, 4
sc.rotation = 0

w = World(800,600,'running', player)
w.add_system('movement', MovementSystem)
w.run()