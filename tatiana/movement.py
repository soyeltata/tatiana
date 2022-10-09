import keyboard
import pygame
from engine import World
from engine.components import TransformComponent, SpriteComponent

def MovementSystem (
    _,
    environment: World
) -> None:
    player = environment.get_entity('mainobj')

    try:
        if keyboard.is_pressed('a'):
            player.get_component(TransformComponent).X -= 1
        
        if keyboard.is_pressed('d'):
            player.get_component(TransformComponent).X += 1
        
        if keyboard.is_pressed('w'):
            player.get_component(TransformComponent).Y -= 1
        
        if keyboard.is_pressed('s'):
            player.get_component(TransformComponent).Y += 1
        
        if keyboard.is_pressed('l'):
            player.get_component(SpriteComponent).rotation += 0.25

        if keyboard.is_pressed('ñ'):
            player.get_component(SpriteComponent).rotation -= 0.25

    except Exception:
        pass