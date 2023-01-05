"""Módulo contenedor de la clase `World`, que tiene como propósito
representar y modelar a un entorno contenedor de entidades y sistemas
en el paradigma **ECS**.
"""
from typing import Dict, List, Tuple, Callable, Optional
from pygame.surface import Surface
import pygame
from .entity import Entity
from .entities import Camera
from .typenames import Self
from .systems import RenderSystem


class World(object):
    """Clase encargada de representar y modelar a un entorno contenedor de
    entidades y sistemas en el paradigma **ECS**, teniendo a su vez como
    propiedades una superficie de pygame (`pygame.surface.Surface`) que
    sirve como pantalla donde será renderizado el contenido, una altura y
    anchura determinada, un color de fondo, una instancia de la clase
    `Camera` como cámara del espacio, una variable limitadora de FPS
    (opcional) así como dos estructuras internas para dicho mecanismo.
    Esto junto con dos diccionarios con cadenas de texto como clave que
    contienen tanto a las entidades del espacio como a los sistemas."""
    screen: Surface
    width: int
    height: int
    bgcolor: Tuple[int, int, int]
    camera: Camera
    entities: Dict[str, Entity]
    systems: Dict[str, Callable[[Surface, Self], None]]
    fpslimit: Optional[int]
    __clock: pygame.time.Clock
    __lasttick: int

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        title: str = "running...",
        mode: int = 0,
        *entities
    ) -> None:
        """Constructor de la clase `World`, toma una anchura y altura que
        serán asignadas a las variables `width` y `height`, un título para
        la ventana junto con un modo de renderizado (pantalla completa, en
        ventana...) y soporta una colección de **entidades** como
        argumentos que se añadirán luego a la propia clase."""
        self.entities = {}
        self.systems = {}
        self.__clock = pygame.time.Clock()
        self.__lasttick = pygame.time.get_ticks()
        self.fpslimit = None
        self.width = width
        self.height = height
        self.bgcolor = (0xff, 0xff, 0xff)
        self.camera = Camera(0, 0)
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), mode)
        self.screen.fill(self.bgcolor)
        pygame.display.set_caption(title)

        for _e in entities:
            self.add_entity(_e)
        self.add_system('render_system', RenderSystem)

    def add_entity(
        self,
        e: Entity
    ) -> None:
        """Función encargada de agregar una entidad al entorno. Añade al
        diccionario `entities` de la clase la entidad pasada como
        argumento teniendo como clave su nombre."""
        self.entities[e.name] = e

    def add_system(
        self,
        name: str,
        s: Callable[[Surface, Self], None]
    ) -> None:
        """Función encargada de agregar un sistema al entorno. Añade al
        diccionario `systems` de la clase el sistema pasado como
        argumento teniendo como clave el nombre pasado también como
        argumento."""
        self.systems[name] = s

    def call_system(
        self,
        name: str
    ) -> None:
        """Función encargada de, a partir de un nombre cualquiera pasado como
        argumento, llamar al sistema asociado con dicho nombre en el
        diccionario `systems` del entorno."""
        self.systems[name](self.screen, self)

    def get_entity(
        self,
        n: str
    ) -> Entity:
        """Función encargada de, a partir de un nombre cualquiera pasado como
        argumento, retornar la entidad asociada con este en el diccionario
        `entities` de la entidad."""
        return self.entities[n]

    def get_entities(
        self
    ) -> List[Entity]:
        """Función que retorna una lista con todas las entidades del entorno,
        con permisos para su mutabilidad ya que no se hace una copia, sino que
        se pasa el original."""
        return list(self.entities.values())

    def get_camera(
        self
    ) -> Camera:
        """Función que retorna la cámara asociada al entorno, esto es, la
        variable `camera`; con permisos para su mutabilidad ya que no se hace
        una copia, sino que se pasa el original."""
        return self.camera

    def set_color(
        self,
        red: int,
        green: int,
        blue: int
    ) -> None:
        """Función encargada de cambiar el color de fondo de la pantalla,
        sirviendo como setter para la variable `bgcolor` de la clase."""
        self.bgcolor = (red, green, blue)

    def set_target_fps(
        self,
        fpslimit: Optional[int] = None
    ) -> None:
        """Función encargada de cambiar el número de fotogramas por segundo
        al que se encuentra limitado el entorno, sirviendo como setter para
        la variable `fpslimit` de la clase."""
        self.fpslimit = fpslimit

    def resize_world(
        self,
        width: int,
        height: int,
        mode: int = 0
    ) -> None:
        """Función encargada de cambiar las dimensiones de la pantalla y el
        modo de renderizado de la misma (este último argumento es opcional,
        si no se introduce nada se tomará el modo por defecto, esto es,
        una ventana flotante)."""
        self.screen = pygame.display.set_mode((width, height), mode)
        self.screen.fill(self.bgcolor)

    @property
    def actual_fps(self) -> float:
        """Función (decorada como propiedad) encargada de retornar el número
        de fotogramas por segundo actuales al que se encuentra ejecutando el
        entorno."""
        return self.__clock.get_fps()

    @property
    def delta_time(self) -> float:
        r"""Función (decorada como propiedad) encargada de retornar el tiempo
        transcurrido entre el anterior fotograma y el actual en segundos,
        lo que se conoce como *"delta time"* o $\Delta t$.
        Calculado mediante la siguiente
        fórmula donde $t_i$ es el tiempo transcurrido desde el inicio y $t_f$
        es el tiempo en el que se llamó por última vez a la función `run`:
        $$\frac{t_i - t_f}{1000}$$"""
        return (pygame.time.get_ticks() - self.__lasttick) / 1000

    def run(
        self
    ) -> None:
        """Función que activa el bucle de eventos principal del entorno, en el
        que se llamarán a todos los sistemas imprimiendo cualquier error en la
        consola para finalmente llamar al sistema de renderizado.
        Posteriormente se registrará la antes mencionada variable $t_f$,
        referida en la clase como `__lasttick`, y se esperará un tiempo
        determinado en función de la variable `fpslimit`."""
        status = True
        while (status):
            for s in self.systems.keys():
                if s == 'render_system':
                    continue
                try:
                    self.call_system(s)
                except Exception as e:
                    print(f'ERROR ON SYSTEM {s}: {e}')

            try:
                self.call_system('render_system')
            except Exception as e:
                print(f'ERROR {e} HAPPENED ON RENDER SYSTEM')

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    status = False

            self.__lasttick = pygame.time.get_ticks()
            if self.fpslimit:
                self.__clock.tick(self.fpslimit)
        pygame.quit()
