from typing import Dict, List, Tuple, Callable, Optional
from pygame.surface import Surface
import pygame
from . import entity
from . import Self
from .systems import RenderSystem
from .entities import Camera


class World(object):
    screen: Surface
    width: int
    height: int
    bgcolor: Tuple[int, int, int]
    camera: Camera
    entities: Dict[str, entity.Entity]
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
        e: entity.Entity
    ) -> None:
        self.entities[e.name] = e

    def add_system(
        self,
        name: str,
        s: Callable[[Surface, Self], None]
    ) -> None:
        self.systems[name] = s

    def call_system(
        self,
        name: str
    ) -> None:
        self.systems[name](self.screen, self)

    def get_entity(
        self,
        n: str
    ) -> entity.Entity:
        return self.entities[n]

    def get_entities(
        self
    ) -> List[entity.Entity]:
        return list(self.entities.values())

    def get_camera(
        self
    ) -> Camera:
        return self.camera

    def set_color(
        self,
        red: int,
        green: int,
        blue: int
    ) -> None:
        self.bgcolor = (red, green, blue)

    def set_target_fps(
        self,
        fpslimit: Optional[int] = None
    ) -> None:
        self.fpslimit = fpslimit

    def resize_world(
        self,
        width: int,
        height: int
    ) -> None:
        self.height = height
        self.width = width
        self.screen = pygame.transform.scale(self.screen, (width, height))

    @property
    def actual_fps(self) -> float:
        return self.__clock.get_fps()

    @property
    def delta_time(self) -> float:
        return (pygame.time.get_ticks() - self.__lasttick) / 1000

    def run(
        self
    ) -> None:
        status = True
        while (status):
            for s in self.systems.keys():
                if s == 'render_system':
                    continue
                self.call_system(s)
            self.call_system('render_system')

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    status = False

            self.__lasttick = pygame.time.get_ticks()
            if self.fpslimit:
                self.__clock.tick(self.fpslimit)
        pygame.quit()
