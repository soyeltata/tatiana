from dataclasses import dataclass as component
from time import time
from typing import Any


@component
class AnimationController:
    begin: int
    end:   int
    speed: float
    condition: Any
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
        self.begin = begin-1
        self.current = begin-1
        self.end = end-1
        self.speed = speed
        self.timestamp = 0
        self.preference = preference

    def set_condition(
        self,
        condition: Any
    ) -> None:
        self.condition = condition

    def set_preference(
        self,
        pref: int
    ) -> None:
        self.preference = pref

    def AnimCondition(
        self,
        condition: Any
    ) -> Any:
        self.condition = condition
        return condition

    def update(self) -> None:
        if (time() - self.timestamp) > self.speed:
            self.current = (self.current - self.begin + 1) \
                         % (self.end - self.begin + 1) \
                         + self.begin
            self.timestamp = time()
