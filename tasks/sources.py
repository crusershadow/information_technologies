from dataclasses import dataclass



@dataclass
class Point:
    x: int = 0
    y: int = 0

    @classmethod
    def from_string(cls, string):
        return cls(*string.split(' '))
