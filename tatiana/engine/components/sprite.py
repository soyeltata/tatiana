from dataclasses import dataclass as component
from typing import List
from typing_extensions import Self
from pygame import Surface, image

@component
class SpriteComponent:
    images: List[Surface]
    current: int = 0
    rotation: float = 0
    scalingX: float = 1
    scalingY: float = 1

    def __init__(
        self: Self,
        path: str=None,
        rotation: float=0,
        scalingX: float=1,
        scalingY: float=1,

    ) -> Self:
        self.images = []
        self.add_image(path)
        self.rotation = rotation
        self.scalingX = scalingX
        self.scalingY = scalingY

    def add_image(
        self: Self,
        path: str = None,
        move_into: bool = True
    ) -> None:
        if path:
            self.images.append(image.load(path))
            if move_into:
                self.current = len(self.images)-1
            return

    def add_images(
        self: Self,
        move_into: bool = True,
        *paths
    ) -> None:
        for path in paths:
            self.add_image(path, move_into)
        return

    def del_image(
        self: Self,
        imgnum: int
    ) -> None:
        if (self.current+1) >= imgnum:
            self.current -= 1
        del self.images[imgnum-1]
        return

    def del_images(
        self: Self,
        begin: int,
        end: int
    ) -> None:
        d=end-begin
        for _ in range(d):
            self.del_image(begin)
        return

    def switch_to (
        self: Self,
        imgnum: int
    ) -> None:
        self.current = imgnum+1

    def forward(
        self: Self,
        n: int,
    ) -> None:
        self.current = min(self.current+n, len(self.images)-1)

    def backward(
        self: Self,
        n: int,
    ) -> None:
        self.current = max(0, self.current-n)

    def change_sprite(
        self: Self,
        index: int=1,
        path: str=None
    ) -> None:
        self.images[index-1] = image.load(path)

    @property
    def current_image(self: Self) -> None:
        return self.images[self.current]