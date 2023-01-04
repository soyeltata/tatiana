import keyboard
from tatiana import World
from tatiana.components import TransformComponent, SpriteComponent

SPEED = 5


def MovementSystem(
    _,
    environment: World
) -> None:
    player = environment.get_entity('mainobj')
    position = player.get_component(TransformComponent)
    # camera = environment.get_camera()

    try:
        if keyboard.is_pressed('a'):
            position.X -= SPEED

        elif keyboard.is_pressed('d'):
            position.X += SPEED

        elif keyboard.is_pressed('w'):
            position.Y -= SPEED

        elif keyboard.is_pressed('s'):
            position.Y += SPEED

    except Exception as e:
        print(e)
