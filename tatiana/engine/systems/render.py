import pygame
from ..components import SpriteComponent, TransformComponent

def RenderSystem (
    screen: pygame.Surface,
    world
) -> None:
    screen.fill(world.bgcolor)
    for entity in world.get_entities():
        img = entity.get_component(SpriteComponent).image
        screen.blit(
            pygame.transform.rotate(pygame.transform.scale(
                img,
                (
                    img.get_width()*entity.get_component(SpriteComponent).scalingX,
                    img.get_height()*entity.get_component(SpriteComponent).scalingY
                )),
                entity.get_component(SpriteComponent).rotation
            ),
            (
                entity.get_component(TransformComponent).X + ((world.width/2)-(img.get_width()/2)),
                entity.get_component(TransformComponent).Y + ((world.height/2)-(img.get_height()/2))
            )
        )
    pygame.display.flip()