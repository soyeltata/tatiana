"""Módulo contenedor de los tipos de datos o `TypeVar`s (no clases)
utilizados en el proyecto.
"""

from typing import TypeVar as __tv
Self = __tv('Self')
"""Al ser el tipo de dato `Self` exclusivo de Python v3.11
y no funcionar del todo bien con mypy, se define en este
módulo como un
[`TypeVar`](https://docs.python.org/es/3/library/typing.html)
cualquiera."""
