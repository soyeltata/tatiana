from typing import Any, Dict, List
import pygame
from ..components import SpriteComponent, TransformComponent

def RenderSystem(
    screen: pygame.Surface,
    world
) -> None:
    pygame.display.flip()
    for entity in world.get_entities():
        screen.blit(entity.get_component(SpriteComponent).image,
            (
                entity.get_component(TransformComponent).X + ((world.width/2)-(entity.get_component(SpriteComponent).image.get_width()/2)),
                entity.get_component(TransformComponent).Y + ((world.height/2)-(entity.get_component(SpriteComponent).image.get_height()/2))
            )
        )