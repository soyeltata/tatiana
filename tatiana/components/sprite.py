from dataclasses import dataclass as component
from typing import List, Optional
from pygame import image
from pygame.surface import Surface
from ..structures.animation import AnimationController


@component
class SpriteComponent:
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
        for path in paths:
            self.add_image(path, move_into)
        return

    def add_animation(
        self,
        animation: AnimationController
    ) -> None:
        self.animations.append(animation)

    def del_image(
        self,
        imgnum: int
    ) -> None:
        if (self.current+1) >= imgnum:
            self.current -= 1
        del self.images[imgnum-1]
        return

    def del_images(
        self,
        begin: int,
        end: int
    ) -> None:
        d = end - begin
        for _ in range(d):
            self.del_image(begin)
        return

    def switch_to(
        self,
        imgnum: int
    ) -> None:
        self.current = imgnum-1

    def forward(
        self,
        n: int,
    ) -> None:
        self.current = abs((self.current + n) % (len(self.images) - 1))

    def backward(
        self,
        n: int,
    ) -> None:
        self.current = abs((self.current - n) % (len(self.images) - 1))

    def change_sprite(
        self,
        index: int = 1,
        path: Optional[str] = None
    ) -> None:
        if not path:
            return
        self.images[index-1] = image.load(path)

    @property
    def current_image(self) -> Surface:
        return self.images[self.current]

    @property
    def height(self) -> int:
        return self.current_image.get_height()

    @property
    def width(self) -> int:
        return self.current_image.get_width()
