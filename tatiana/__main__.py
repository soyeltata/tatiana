from world import World
from entity import Entity

w = World(800,600,'running',Entity('base',(0,0),'base.png'))
w.set_color(0xff, 0xff, 0xff)
w.run()