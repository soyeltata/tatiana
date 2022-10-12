from dataclasses import dataclass as component
from time import time
from typing import Any
from typing_extensions import Self

@component
class AnimationController:
    begin: int
    end:   int
    speed: float
    condition: Any
    current: int
    timestamp: float

    def __init__(
        self: Self,
        begin: int,
        end: int,
        speed: float
    ) -> None:
        self.begin = begin-1
        self.current = begin-1
        self.end = end-1
        self.speed = speed
        self.timestamp = 0

    def set_condition(
        self: Self,
        condition: Any
    ) -> None:
        self.condition = condition

    def AnimCondition(
        self: Self,
        condition: Any
    ) -> Any:
        self.condition = condition
        return condition

    def update(self: Self) -> None:
        if (time() - self.timestamp) > self.speed:
            self.current = (self.current - self.begin + 1) % (self.end - self.begin + 1) + self.begin
            self.timestamp = time()