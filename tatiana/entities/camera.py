"""Módulo contenedor de la clase `Camera`, encargada de representar
y modelar el funcionamiento de una cámara en dos dimensiones."""
from dataclasses import dataclass


@dataclass
class Camera(object):
    """Clase encargada de representar y modelar el funcionamiento de la
    cámara en un entorno de dos dimensiones, contando con un componente
    $x$ e $y$ y siendo definida como un `dataclass` para más simplicidad."""
    X: float
    Y: float
