from engine import World, Entity
from movement import MovementSystem
from os.path import abspath

player = Entity('mainobj', (0, 0), abspath('assets/main.png'))

w = World(800,600,'running', player)
w.add_system('movement', MovementSystem)
w.run()