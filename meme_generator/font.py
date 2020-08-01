from enum import Enum


class Font(Enum):
    IMPACT = "fonts/impact.ttf"

    def __str__(self):
        return str(self.value)
