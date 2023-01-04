"""
**Tatiana** es un pequeño intento de implementar un
motor de videojuegos 2D competente utilizando **Python**
(en una versión superior o igual a **3.10**) y el módulo
**pygame** como dependencia obligatoria, además de estar
construido y regirse enteramente mediante el paradigma
**ECS** (en castellano: *sistema entidad-componente*).

Como es obvio debido a la versión en la que actualmente
se encuentra este proyecto, debe tratarse por el momento
como una prueba de concepto más que como un producto
estable y seguro, pues todavía quedan multitud de
funcionalidades esenciales en cualquier motor de videojuegos
por implementar a la par que muchos errores (que podrían ser
considerados como graves) por corregir; por no mencionar el
detalle de estar escrito enteramente en **Python**, lo que
hace de este motor algo lento en comparación.

No obstante y a causa de los importantes avances que ha
estado teniendo este proyecto, he decidido hacer público
este proyecto para facilitar su uso y, en caso de tener
sugerencias para el mismo o querer asistir en el desarrollo,
hacer posible la contribución por parte de cualquiera.
"""
from .world import World
from .entity import Entity
from . import systems
from . import components
from . import structures
from . import typenames
