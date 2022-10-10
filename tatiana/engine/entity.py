from typing import Any, Dict, Tuple
from typing_extensions import Self
from . import components

class Entity:
    name: str
    components: Dict[Any, Any]
    properties: Dict[str, Any]

    def __init__(
        self: Self,
        name: str,
        position: Tuple[float] = (0,0),
        sprite_path: str       = None,
        *ocomponents
    ) -> Self:
        self.name = name
        self.components = {}
        self.properties = {}

        self.add_component(components.TransformComponent(*position))

        if sprite_path:
            self.add_component(components.SpriteComponent(sprite_path))

        for component in ocomponents:
            self.add_component(component)

    def add_component(self: Self, component, *args):
        key = type(component)
        self.components[key] = component

    def get_component(self: Self, clazz):
        return self.components[clazz]

    def has_component(self: Self, clazz):
        return self.get_component(clazz) is not None

    def change_sprite(self: Self, path: str) -> None:
        if self.has_component(components.SpriteComponent):
            self.components[components.SpriteComponent].change_sprite(1, path)

    def set_property(self: Self, name: str, value: Any) -> None:
        self.properties[name] = value

    def get_property(self: Self, name: str) -> None:
        try:
            return self.properties[name]
        except Exception:
            return None