"""Módulo contenedor de la clase `Entity`, que tiene como propósito
representar y modelar a una entidad cualquiera en el paradigma **ECS**.
"""
from typing import Any, Dict, Tuple, Optional
from . import components


class Entity:
    """Clase encargada de representar y modelar una entidad cualquiera
    en el paradigma **ECS**, teniendo a su vez como propiedades un **nombre**,
    una colección de **componentes** y propiedades varias para información
    adicional que deba de contener."""
    name: str
    components: Dict[Any, Any]
    """Debido a la carencia de tipos de datos suficientes para modelar esta
    situación, nos vemos obligados a describir el diccionario de componentes
    como uno de tipos `Any` y `Any` para su clave y valor, sin embargo, lo que
    se quiere representar es un diccionario que tomará una clase como clave y
    una instancia de la misma como valor."""
    properties: Dict[str, Any]

    def __init__(
        self,
        name: str,
        position: Tuple[float, float] = (.0, .0),
        sprite_path: Optional[str] = None,
        *ocomponents
    ) -> None:
        """Constructor de la clase `Entity`, toma un nombre que será asignado
        a la variable `name` del mismo objeto, una posición que se añadirá
        a los componentes como un `TransformComponent`, una dirección
        (opcional) hacia el sprite del dicho objeto que se agregará como un
        `SpriteComponent` y soporta una colección de componentes como
        argumentos que se asignarán luego a la propia entidad."""
        self.name = name
        self.components = {}
        self.properties = {}

        self.add_component(components.TransformComponent(*position))

        if sprite_path:
            self.add_component(components.SpriteComponent(sprite_path))

        for component in ocomponents:
            self.add_component(component)

    def add_component(self, component: Any) -> None:
        """Función encargada de agregar un componente a la entidad. Añade al
        diccionario `components` de la clase el componente pasado como
        argumento teniendo como clave su clase."""
        key = type(component)
        self.components[key] = component

    def get_component(self, clazz: Any) -> Any:
        """Función encargada de, a partir de una clase cualquiera pasada como
        argumento, retornar el componente asociado a esta en el diccionario
        `components` de la entidad."""
        try:
            return self.components[clazz]
        except KeyError:
            return None

    def has_component(self, clazz: Any) -> bool:
        """Función encargada de, a partir de una clase cualquiera pasada como
        argumento, retornar un valor booleano que represente si existe un
        componente asociado a esta."""
        return self.get_component(clazz) is not None

    def change_sprite(self, path: str) -> None:
        """Función encargada de, a partir de una ruta determinada como una
        cadena de texto, cambiar el sprite de la entidad por la imagen a la
        que apunta la dicha ruta."""
        if self.has_component(components.SpriteComponent):
            self.components[components.SpriteComponent].change_sprite(1, path)

    def set_property(self, name: str, value: Any) -> None:
        """Función encargada de asignar una propiedad a la entidad, sirviendo
        como setter para el diccionario `properties` de la clase."""
        self.properties[name] = value

    def get_property(self, name: str) -> Optional[Any]:
        """Función encargada de retornar una propiedad determinada de la
        entidad, sirviendo como getter para el diccionario `properties` de
        la clase."""
        try:
            return self.properties[name]
        except KeyError:
            return None

    def has_property(self, name: str) -> bool:
        """Función encargada de retornar un valor booleano que determine
        si existe una propiedad asociada al nombre pasado como argumento
        en el diccionario `properties` de la clase."""
        return self.get_property(name) is not None
