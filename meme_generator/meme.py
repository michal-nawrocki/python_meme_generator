from PIL import (
    Image,
    ImageDraw,
    ImageFilter,
    ImageFont,
    UnidentifiedImageError
)
import sys

from font import Font
from meme_template import MemeTemplate


class Meme:
    def __init__(self, template: MemeTemplate):
        try:
            self.img = Image.open(str(template))
        except (FileNotFoundError, ValueError, UnidentifiedImageError) as e:
            print("Couldn't load Image. Exiting...")
            sys.exit(1)

    def set_font(self, font: Font, size: int):
        try:
            self.font = ImageFont.truetype(font=str(font), size=size)
        except OSError:
            print("Couldn't load Font. Exiting...")
            sys.exit(1)
