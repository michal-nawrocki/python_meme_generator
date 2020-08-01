from PIL import (
    Image,
    ImageDraw,
    ImageFilter,
    ImageFont,
    UnidentifiedImageError
)
import sys
import textwrap

from font import Font
from meme_template import MemeTemplate


class Meme:
    """
    Main class for a Meme. Contains all relevant functions to construct a meme
    """

    def __init__(self, template: MemeTemplate, font: Font = None):
        self.set_meme_template(template)
        self._make_image_draw()

        if font:
            self.set_font(font)

    def set_meme_template(self, template: MemeTemplate):
        try:
            self.img = Image.open(str(template))
        except (FileNotFoundError, ValueError, UnidentifiedImageError) as e:
            print("Couldn't load Image. Exiting...")
            sys.exit(1)

        self.img_width, self.img_height = self.img.size

    def set_font(self, font: Font, size: int = None):
        if not size:
            size = int(self.img_height/10)

        try:
            self.font = ImageFont.truetype(font=str(font), size=size)
        except OSError:
            print("Couldn't load Font. Exiting...")
            sys.exit(1)

        self.char_width, self.char_height = self.font.getsize("A")

    def _make_image_draw(self):
        self.draw = ImageDraw.Draw(self.img)

    def _prepare_text(self, top_text: str, bottom_text: str):
        top_text = top_text.upper()
        bottom_text = bottom_text.upper()

        max_chars_on_line = self.img_width // self.char_width

        top = textwrap.wrap(top_text, width=max_chars_on_line)
        bottom = textwrap.wrap(bottom_text, width=max_chars_on_line)

        return top, bottom

    def _draw_lines(self, lines, start_y):
        y = start_y

        for line in lines:
            line_width, line_height = self.font.getsize(line)
            x = (self.img_width - line_width)/2
            self._draw_shadow(x, y, line, "black")
            self.draw.text((x, y), line, fill="white", font=self.font)
            y += line_height

    def _draw_shadow(self, x, y, line, background_color):
        """
        Draw shadow for text to be visibile on all templates
        """
        self.draw.text((x-1, y-1), line, font=self.font, fill=background_color)
        self.draw.text((x+1, y-1), line, font=self.font, fill=background_color)
        self.draw.text((x-1, y+1), line, font=self.font, fill=background_color)
        self.draw.text((x+1, y+1), line, font=self.font, fill=background_color)

    def write_text(self, top_text: str, bottom_text: str):
        top, bottom = self._prepare_text(top_text, bottom_text)
        y = 0
        self._draw_lines(top, y)

        y = self.img_height - self.char_height * len(bottom) - 5
        self._draw_lines(bottom, y)
