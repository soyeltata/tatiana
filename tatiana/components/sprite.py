"""Módulo contenedor del componente básico `SpriteComponent`,
encargado de representar la imagen (o colección de imágenes),
junto con el conjunto de animaciones que tendrá una entidad."""
from dataclasses import dataclass as component
from typing import List, Optional
from pygame import image
from pygame.surface import Surface
from ..structures.animation import AnimationController


@component
class SpriteComponent:
    """Componente básico encargado de representar la imagen
    (o colección de imágenes), junto con el conjunto de animaciones
    que tendrá una entidad. Esta clase consta de una lista de
    imágenes (`pygame.surface.Surface`) junto con una lista de
    animaciones (controladores de animaciones, esto es,
    `AnimationController`), un índice para la imagen actual, una
    variable para indicar la rotación del sprite junto con otras
    dos para representar el escalado, el *"layer"* en el que se
    encuentra el sprite y una variable para la opacidad del mismo."""
    images: List[Surface]
    animations: List[AnimationController]
    current: int = 0
    rotation: float = 0
    scalingX: float = 1
    scalingY: float = 1
    layer: int = 0
    opacity: int = 100

    def __init__(
        self,
        path: Optional[str] = None,
        rotation: float = 0,
        scalingX: float = 1,
        scalingY: float = 1,
        opacity: int = 100,
        layer: int = 0
    ) -> None:
        """Constructor del componente `SpriteComponent`, toma una ruta
        (opcional) hacia una imagen que luego será añadida al componente,
        una rotación, escalado y opacidad que luego serán asignadas a sus
        respectivas variables y un entero indicando la capa en la que se
        encuentra."""
        self.images = []
        self.animations = []
        self.add_image(path)
        self.rotation = rotation
        self.scalingX = scalingX
        self.scalingY = scalingY
        self.opacity = opacity
        self.layer = layer

    def add_image(
        self,
        path: Optional[str] = None,
        move_into: bool = True
    ) -> None:
        """Función encargada de añadir una imagen al componente, toma una
        ruta (opcional) hacia la imagen a añadir y un valor booleano que
        indica si se desea mover el puntero de la imagen actual hacia la
        nueva añadida."""
        if path:
            self.images.append(image.load(path))
            if move_into:
                self.current = len(self.images)-1
            return

    def add_images(
        self,
        move_into: bool = True,
        *paths
    ) -> None:
        """Función con el mismo comportamiento que `add_image`, pero para
        un grupo de imágenes en vez de una sola."""
        for path in paths:
            self.add_image(path, move_into)

    def add_animation(
        self,
        animation: AnimationController
    ) -> None:
        """Función encargada de añadir una animación a la lista de
        animaciones del componente. Toma como único argumento la animación
        a añadir."""
        self.animations.append(animation)

    def del_image(
        self,
        imgnum: int
    ) -> None:
        """Función encargada de eliminar una de las imágenes de la lista.
        Toma como único parámetro el índice de la imagen a eliminar."""
        if (self.current+1) >= imgnum:
            self.current -= 1
        del self.images[imgnum-1]

    def del_images(
        self,
        begin: int,
        end: int
    ) -> None:
        """Función con el mismo comportamiento que `del_image` pero para
        un grupo de imágenes en vez de una sola."""
        d = end - begin
        for _ in range(d):
            self.del_image(begin)

    def switch_to(
        self,
        imgnum: int
    ) -> None:
        """Función encargada de mover el puntero de imagen hacia una
        posición en específico determinada por el argumento de la
        función."""
        self.current = imgnum-1

    def forward(
        self,
        n: int,
    ) -> None:
        r"""Función con un comportamiento similar al de `switch_to`, pero
        moviendo el puntero hacia adelante en `n` posiciones. El nuevo
        índice es calculado mediante la siguiente fórmula, siendo $c$ el
        índice del puntero y $l$ el número total de imágenes:
        $$\lvert (c + n) \mod{(l - 1)} \rvert$$"""
        self.current = abs((self.current + n) % (len(self.images) - 1))

    def backward(
        self,
        n: int,
    ) -> None:
        r"""Función con un comportamiento similar al de `switch_to`, pero
        moviendo el puntero hacia atrás en `n` posiciones. El nuevo
        índice es calculado mediante la siguiente fórmula, siendo $c$ el
        índice del puntero y $l$ el número total de imágenes:
        $$\lvert (c - n) \mod{(l - 1)} \rvert$$"""
        self.current = abs((self.current - n) % (len(self.images) - 1))

    def change_sprite(
        self,
        index: int = 1,
        path: Optional[str] = None
    ) -> None:
        """Función encargada de cambiar el una imagen determinada de la
        lista, referenciada a través de un índice pasado como argumento,
        para sustituirla por una imagen situada en una ruta también pasada
        como argumento."""
        if not path:
            return
        self.images[index-1] = image.load(path)

    @property
    def current_image(self) -> Surface:
        """Función (decorada como propiedad) que retorna la imagen actual
        a la que apunta el puntero."""
        return self.images[self.current]

    @property
    def height(self) -> int:
        """Función (decorada como propiedad) que retorna la altura de la
        imagen a la que apunta el puntero."""
        return self.current_image.get_height()

    @property
    def width(self) -> int:
        """Función (decorada como propiedad) que retorna la anchura de la
        imagen a la que apunta el puntero."""
        return self.current_image.get_width()
