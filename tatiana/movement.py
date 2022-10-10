import keyboard
import time
from engine import World
from engine.components import TransformComponent, SpriteComponent

SPEED = 5   # player speed
ANSPD = .5  # animation speed

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
            ts = player.get_property('timestamp')
            if ts:
                if (time.time() - ts[1]) > ANSPD or (ts[0] != 'a'):
                    player.set_property('timestamp', ('a',time.time()))
                    if not (3 <= sprite.current <= 5):
                        sprite.switch_to(4)
                    sprite.current = (sprite.current-2)%(3)+3
            else:
                player.set_property('timestamp', ('a',time.time()))
            position.X -= SPEED
            camera.X -= SPEED
        
        elif keyboard.is_pressed('d'):
            sprite.scalingX = pos(sprite.scalingX)
            ts = player.get_property('timestamp')
            if ts:
                if (time.time() - ts[1]) > ANSPD or (ts[0] != 'd'):
                    player.set_property('timestamp', ('d',time.time()))
                    if not (3 <= sprite.current <= 5):
                        sprite.switch_to(4)
                    sprite.current = (sprite.current-2)%(3)+3
            else:
                player.set_property('timestamp', ('d',time.time()))
            position.X += SPEED
            camera.X += SPEED
        
        elif keyboard.is_pressed('w'):
            sprite.scalingX = pos(sprite.scalingX)
            ts = player.get_property('timestamp')
            if ts:
                if (time.time() - ts[1]) > ANSPD or (ts[0] != 'w'):
                    player.set_property('timestamp', ('w',time.time()))
                    if not (7 <= sprite.current <= 8):
                        sprite.switch_to(8)
                    sprite.current = (sprite.current-6)%(2)+7
            else:
                player.set_property('timestamp', ('w', time.time()))
            position.Y -= SPEED
            camera.Y -= SPEED
        
        elif keyboard.is_pressed('s'):
            sprite.scalingX = pos(sprite.scalingX)
            ts = player.get_property('timestamp')
            if ts:
                if (time.time() - ts[1]) > ANSPD or (ts[0] != 's'):
                    player.set_property('timestamp', ('s',time.time()))
                    if not (1 <= sprite.current <= 2):
                        sprite.switch_to(2)
                    sprite.current = (sprite.current)%(2)+1
            else:
                player.set_property('timestamp', ('s',time.time()))
            position.Y += SPEED
            camera.Y += SPEED

        else:
            ts = player.get_property('timestamp')
            if ts:
                if (time.time() - ts[1]) > ANSPD/2:
                    player.set_property('timestamp', ('none', time.time()))
                    sprite.switch_to(1)
            else:
                player.set_property('timestamp', ('none', time.time()))

    except Exception as e:
        print(e)