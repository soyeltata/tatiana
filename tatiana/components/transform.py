"""Módulo contenedor del componente básico `TransformComponent`,
encargado de representar la posición de una entidad en el espacio
bidimensional."""
from dataclasses import dataclass as component
from typing import Tuple


@component
class TransformComponent:
    """Componente básico de todas las entidades encargado de representar
    la posición en el espacio de dicha entidad. Sustituto a un vector
    bidimensional, con coordenadas $x$ e $y$."""
    X: float = 0
    Y: float = 0

    @property
    def as_tuple(self) -> Tuple[float, float]:
        """Función encargada de representar este componente en forma de
        una tupla de dos elementos, de nuevo, $x$ e $y$."""
        return self.X, self.Y
