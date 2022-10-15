from dataclasses import dataclass as component

@component
class TransformComponent:
    X: float = 0
    Y: float = 0

    @property
    def as_tuple(self) -> tuple:
        return self.X, self.Y