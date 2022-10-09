import pygame
from ..components import SpriteComponent, TransformComponent

def RenderSystem (
    screen: pygame.Surface,
    world
) -> None:
    screen.fill(world.bgcolor)
    for entity in world.get_entities():
        screen.blit(entity.get_component(SpriteComponent).image,
            (
                entity.get_component(TransformComponent).X + ((world.width/2)-(entity.get_component(SpriteComponent).image.get_width()/2)),
                entity.get_component(TransformComponent).Y + ((world.height/2)-(entity.get_component(SpriteComponent).image.get_height()/2))
            )
        )
    pygame.display.flip()