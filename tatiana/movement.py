import keyboard
import time
from engine import World
from engine.components import TransformComponent, SpriteComponent

SPEED = 5   # player speed
ANSPD = .5  # animation speed

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
            ts = player.get_property('timestamp')
            if ts:
                if (time.time() - ts) > ANSPD:
                    player.set_property('timestamp', time.time())
                    print(sprite.current)
                    sprite.switch_to((sprite.current+1) % 3 + 2)
            else:
                player.set_property('timestamp', time.time())

            position.X -= SPEED
            camera.X -= SPEED
        
        elif keyboard.is_pressed('d'):
            position.X += SPEED
            camera.X += SPEED
        
        elif keyboard.is_pressed('w'):
            position.Y -= SPEED
            camera.Y -= SPEED
        
        elif keyboard.is_pressed('s'):
            position.Y += SPEED
            camera.Y += SPEED

        else:
            ts = player.get_property('timestamp')
            if ts:
                if (time.time() - ts) > ANSPD:
                    player.set_property('timestamp', time.time())
                    sprite.switch_to(1)
            else:
                player.set_property('timestamp', time.time())

    except Exception as e:
        print(e)