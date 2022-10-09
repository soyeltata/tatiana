from typing import Any, Dict, List, Tuple
from typing_extensions import Self
from pygame import Surface
import pygame
from . import entity
from .systems import RenderSystem

class World(object):
    screen: Surface
    width:int
    height:int
    bgcolor: Tuple[int]
    entities: Dict[str, entity.Entity]
    systems: Dict[str, Any]

    def __init__(
        self: Self,
        width:  int=800,
        height: int=600,
        title: str="running...",
        *entities
    ) -> Self:
        self.entities={}
        self.systems={}
        self.width=width
        self.height=height
        self.bgcolor=(0xff,0xff,0xff)
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
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
        return list(self.entities.values())

    def set_color(
        self: Self,
        red: int,
        green: int,
        blue: int
    ) -> None:
        self.bgcolor = (red, green, blue)

    def run(
        self: Self
    ) -> None:
        status = True
        while (status):
            for s in self.systems.keys():
                self.call_system(s)

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    status = False
        pygame.quit()