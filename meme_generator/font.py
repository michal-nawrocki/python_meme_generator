from enum import Enum


class Font(Enum):
    """
    Enum to get location of available `.ttf` fonts
    """

    IMPACT = "../fonts/impact.ttf"
    COMIC_SANS = "../fonts/comic_sans.ttf"

    def __str__(self):
        return str(self.value)
