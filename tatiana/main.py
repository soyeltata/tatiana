from keyboard import is_pressed
from engine import World, Entity
from engine.components import SpriteComponent, TransformComponent
from engine.structures import AnimationController
from movement import MovementSystem
from os.path import abspath

RESX = 800
RESY = 600
p = lambda x: abspath(f'assets/{x}.png')

player = Entity('mainobj', (0, 0), p('bbox_down_idle'))
pos = player.get_component(TransformComponent)
sc = player.get_component(SpriteComponent)
sc.scalingX, sc.scalingY = 5, 5

sc.add_images(False,
    p('bbox_down1'),
    p('bbox_down2'),
    p('bbox_lateral_idle'),
    p('bbox_lateral1'),
    p('bbox_lateral2'),
    p('bbox_up_idle'),
    p('bbox_up1'),
    p('bbox_up2')
)

an1 = AnimationController(2, 3, .5)
an1.set_condition(lambda _: is_pressed('s'))
sc.add_animation(an1)

an2 = AnimationController(8, 9, .5)
an2.set_condition(lambda _: is_pressed('w'))
sc.add_animation(an2)

an3 = AnimationController(5, 6, .5)
an3.set_condition(lambda _: is_pressed('a') or is_pressed('d'))
sc.add_animation(an3)

an4 = AnimationController(1, 1, .5)
an4.set_condition(lambda _: True)
sc.add_animation(an4)

bg = Entity('bg', (-RESX/2, -RESY/2), p('bg'))
sc2 = bg.get_component(SpriteComponent)
sc2.scalingX, sc2.scalingY = 50, 50
sc2.layer = -1

w = World(RESX,RESY,'running')
w.add_entity(player)
w.add_entity(bg)
w.add_system('movement', MovementSystem)
w.run()