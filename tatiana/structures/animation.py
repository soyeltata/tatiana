"""Módulo contenedor de la clase `AnimationController`, encargada de
gestionar una animación en una colección de imágenes."""
from dataclasses import dataclass
from time import time
from typing import Callable, Any


@dataclass
class AnimationController:
    """Clase encargada de gestionar una única animación en una
    colección de imágenes, esto es, en un `SpriteComponent`."""
    begin: int
    end: int
    speed: float
    condition: Callable[[Any], bool]
    current: int
    timestamp: float
    preference: int

    def __init__(
        self,
        begin: int,
        end: int,
        speed: float,
        preference: int = 0
    ) -> None:
        """Constructor de la clase `AnimationController`, que toma
        como argumentos cuatro de las siete propiedades de la clase
        y se las asigna (el inicio de la animación, el final, la
        velocidad y la preferencia que tiene esa animación con
        respecto a las demás), además, también inicializa la imágen
        actual y el `timestamp`, esta última con el propósito de
        que pueda fluir la animación."""
        self.begin = begin-1
        self.current = begin-1
        self.end = end-1
        self.speed = speed
        self.timestamp = 0
        self.preference = preference

    def set_condition(
        self,
        condition: Callable[[Any], bool]
    ) -> None:
        """Función encargada de, dada una función que cumpla con
        los requerimientos de los tipos de datos (que tome una
        entidad como argumento y retorne un valor booleano),
        asignársela a la animación como condición para que se
        ejecute."""
        self.condition = condition

    def set_preference(
        self,
        pref: int
    ) -> None:
        """Función encargada de cambiar la preferencia con la que
        se ejecutará la animación en cuestión, puede pensarse este
        dato como el *"layer"* de un sprite."""
        self.preference = pref

    def AnimCondition(
        self,
        condition: Callable[[Any], bool]
    ) -> Callable[[Any], bool]:
        """Exactamente el mismo funcionamiento de la función
        `set_condition`, pero en forma de decorador."""
        self.condition = condition
        return condition

    def update(self) -> None:
        r"""Función encargada de, si ha pasado el tiempo suficiente,
        actualizar la imagen a la que apunta la animación a la
        siguiente mediante la siguiente fórmula, en la que $e$
        representa el índice de la animación final, $b$ el de la
        inicial y $c$ el de la actual:
        $$ (c - b + 1) \mod{(e - b + 1)} + b $$"""
        if (time() - self.timestamp) > self.speed:
            self.current = (self.current - self.begin + 1) \
                         % (self.end - self.begin + 1) \
                         + self.begin
            self.timestamp = time()
