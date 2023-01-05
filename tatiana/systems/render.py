"""Módulo contenedor del sistema fundamental `RenderSystem`, encargado
de renderizar todas las entidades del entorno en pantalla."""
import pygame
from ..components import SpriteComponent, TransformComponent


def RenderSystem(
    screen: pygame.surface.Surface,
    world
) -> None:
    """Sistema fundamental del motor encargado de renderizar todas
    las entidades del entorno en pantalla. Primero rellena el fondo
    con el color de fondo, valga la redundancia, siendo este la
    propiedad `bgcolor` del argumento `world`, luego itera a través
    de todas las entidades ordenadas a partir del layer en el que se
    sitúan y le aplica tanto la animación que tenga lugar como las
    diferentes propiedades que tenga su `SpriteComponent`.
    Finalmente las dibuja en pantalla."""
    screen.fill(world.bgcolor)
    cmr = world.get_camera()
    for entity in sorted(world.get_entities(),
                         key=(lambda e: e.get_component(SpriteComponent)
                                         .layer)):
        img = None
        sc = entity.get_component(SpriteComponent)
        active = list(sorted(list(filter(lambda anim: anim.condition(entity),
                                         sc.animations)),
                             key=(lambda a: a.preference),
                             reverse=True))
        if not len(active):
            img = pygame.transform.flip(sc.current_image,
                                        sc.scalingX < 0,
                                        sc.scalingY < 0)
        else:
            img = pygame.transform.flip(sc.images[active[0].current],
                                        sc.scalingX < 0,
                                        sc.scalingY < 0)
            active[0].update()

        renderimage = \
            pygame.transform.rotate(pygame.transform.scale(
                img,
                (
                    img.get_width()*abs(sc.scalingX),
                    img.get_height()*abs(sc.scalingY)
                )),
                sc.rotation
            )
        renderimage.set_alpha(int(sc.opacity * (255/100)))

        screen.blit(
            renderimage,
            (
                entity.get_component(TransformComponent).X
                + ((world.width / 2) - (img.get_width() / 2))
                - cmr.X,

                entity.get_component(TransformComponent).Y
                + ((world.height / 2) - (img.get_height() / 2))
                - cmr.Y
            )
        )
    pygame.display.flip()
