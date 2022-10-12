import keyboard
from engine import World
from engine.components import TransformComponent, SpriteComponent

SPEED = 5

neg = lambda n: -n if n >= 0 else n
pos = lambda n: n if n >= 0 else -n

def MovementSystem (
    _,
    environment: World
) -> None:
    player = environment.get_entity('mainobj')
    position = player.get_component(TransformComponent)
    sprite = player.get_component(SpriteComponent)
    camera = environment.get_entity('camera')

    try:
        if keyboard.is_pressed('a'):
            sprite.scalingX = neg(sprite.scalingX)
            position.X -= SPEED
            camera.X -= SPEED
        
        elif keyboard.is_pressed('d'):
            sprite.scalingX = pos(sprite.scalingX)
            position.X += SPEED
            camera.X += SPEED
        
        elif keyboard.is_pressed('w'):
            sprite.scalingX = pos(sprite.scalingX)
            position.Y -= SPEED
            camera.Y -= SPEED
        
        elif keyboard.is_pressed('s'):
            sprite.scalingX = pos(sprite.scalingX)
            position.Y += SPEED
            camera.Y += SPEED

    except Exception as e:
        print(e)