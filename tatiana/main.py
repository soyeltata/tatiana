from engine import World, Entity
from engine.components import SpriteComponent, TransformComponent
from movement import MovementSystem
from os.path import abspath

RESX = 800
RESY = 600
p = lambda x: abspath(f'assets/{x}.png')

player = Entity('mainobj', (0, 0), p('bbox_down_idle'))
pos = player.get_component(TransformComponent)
sc = player.get_component(SpriteComponent)
pos.X, pos.Y = pos.X-(sc.width/2), pos.Y-(sc.height/2)
sc.scalingX, sc.scalingY = 5, 5

sc.add_images(False, p('bbox_down1'), p('bbox_down2'), p('bbox_lateral_idle'), p('bbox_lateral1'), p('bbox_lateral2'), p('bbox_up_idle'), p('bbox_up1'), p('bbox_up2'))

bg = Entity('bg', (-RESX/2, -RESY/2), p('bg'))
sc2 = bg.get_component(SpriteComponent)
sc2.scalingX, sc2.scalingY = 50, 50
sc2.layer = -1

w = World(RESX,RESY,'running')
w.add_entity(player)
w.add_entity(bg)
w.add_system('movement', MovementSystem)
w.run()