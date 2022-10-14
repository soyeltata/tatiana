from typing import Any, Dict, List, Tuple
from typing_extensions import Self
from pygame import Surface
import pygame
from . import entity
from .systems import RenderSystem
from .entities import Camera

class World(object):
    screen: Surface
    width:int
    height:int
    bgcolor: Tuple[int]
    entities: Dict[str, entity.Entity]
    systems: Dict[str, Any]
    fpslimit: float
    __clock: pygame.time.Clock

    def __init__(
        self: Self,
        width:  int=800,
        height: int=600,
        title: str="running...",
        mode: int=0,
        *entities
    ) -> Self:
        self.entities={}
        self.systems={}
        self.__clock=pygame.time.Clock()
        self.fpslimit=0
        self.width=width
        self.height=height
        self.bgcolor=(0xff,0xff,0xff)
        self.entities['camera'] = Camera(0, 0)
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), mode)
        self.screen.fill(self.bgcolor)
        pygame.display.set_caption(title)

        for _e in entities:
            self.add_entity(_e)
        self.add_system('render_system', RenderSystem)

    def add_entity(
        self: Self,
        e: entity.Entity
    ) -> None:
        self.entities[e.name] = e

    def add_system(
        self: Self,
        name: str,
        s: Any
    ) -> None:
        self.systems[name] = s

    def call_system(
        self: Self,
        name: str
    ) -> None:
        self.systems[name](self.screen, self)

    def get_entity(
        self: Self,
        n: str
    ) -> entity.Entity:
        return self.entities[n]

    def get_entities(
        self: Self
    ) -> List[entity.Entity]:
        res = []
        for ent in self.entities.values():
            if ent is self.entities['camera']:
                continue
            res.append(ent)
        return res

    def set_color(
        self: Self,
        red: int,
        green: int,
        blue: int
    ) -> None:
        self.bgcolor = (red, green, blue)

    def set_target_fps(
        self: Self,
        fpslimit: float=0
    ) -> None:
        self.fpslimit = fpslimit

    @property
    def actual_fps(self: Self) -> float:
        return self.__clock.get_fps()

    def resize_world(
        self: Self,
        width: int,
        height: int
    ) -> None:
        self.height = height
        self.width = width
        self.screen = pygame.transform.scale(self.screen, (width, height))

    def run(
        self: Self
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
            
            if self.fpslimit:
                self.__clock.tick(self.fpslimit)
        pygame.quit()