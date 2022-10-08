from dataclasses import dataclass as component
from typing_extensions import Self
from pygame import Surface, image

@component
class SpriteComponent:
    image: Surface
    rotation: float = 0
    scaling: float = 0

    def __init__(
        self: Self,
        path: str,
        rotation: float=0,
        scaling: float=0
    ) -> Self:
        self.image = image.load(path)
        self.rotation = rotation
        self.scaling = scaling