from typing import Any, Dict, Tuple
from typing_extensions import Self
from . import components

class Entity:
    name: str
    components: Dict[Any, Any]

    def __init__(
        self: Self,
        name: str,
        position: Tuple[float] = (0,0),
        sprite_path: str       = None,
        *ocomponents
    ) -> Self:
        self.name = name
        self.components = {}

        self.add_component(components.TransformComponent(*position))

        if sprite_path:
            self.add_component(components.SpriteComponent(sprite_path))

        for component in ocomponents:
            self.set_component(component)

    def add_component(self, component, *args):
        key = type(component)
        self.components[key] = component

    def get_component(self, clazz):
        return self.components[clazz]

    def has_component(self, clazz):
        return self.get_component(clazz) is not None