import pygame
from ..components import SpriteComponent, TransformComponent

def RenderSystem (
    screen: pygame.Surface,
    world
) -> None:
    screen.fill(world.bgcolor)
    cmr = world.get_entity('camera')
    for entity in sorted(world.get_entities(), key=(lambda e: e.get_component(SpriteComponent).layer)):
        img = None
        sc = entity.get_component(SpriteComponent)
        active = list(filter(lambda anim: anim.condition(entity), sc.animations))
        if not len(active):
            img = pygame.transform.flip(sc.current_image, sc.scalingX<0, sc.scalingY<0)
        else:
            img = pygame.transform.flip(sc.images[active[0].current], sc.scalingX<0, sc.scalingY<0)
            active[0].update()

        screen.blit(
            pygame.transform.rotate(pygame.transform.scale(
                img,
                (
                    img.get_width()*abs(sc.scalingX),
                    img.get_height()*abs(sc.scalingY)
                )),
                sc.rotation
            ),
            (
                entity.get_component(TransformComponent).X + ((world.width/2)-(img.get_width()/2)) - cmr.X,
                entity.get_component(TransformComponent).Y + ((world.height/2)-(img.get_height()/2)) - cmr.Y
            )
        )
    pygame.display.flip()