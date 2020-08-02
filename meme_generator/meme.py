from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import textwrap

from font import Font
from meme_template import MemeTemplate


class Meme:
    """
    Main class for a Meme. Contains all relevant functions to construct a meme
    """

    def __init__(self, template: MemeTemplate, font: Font = Font.IMPACT):
        """
        Create all necessary members for drawing text to image.
        This includes - The `MemeTemplate` Image, ImageFont, and ImageDraw objects

        :param template A MemTemplate enum
        :param font A Font enum
        """

        self._set_meme_template(template)
        self._make_image_draw()

        if font:
            self._set_font(font)

    def _set_meme_template(self, template: MemeTemplate):
        """
        Set the MemeTemplate for this Meme object from the MemeTemplate enums

        :param template MemeTemplate enum
        """

        try:
            self.img = Image.open(str(template))
        except (FileNotFoundError, ValueError, UnidentifiedImageError) as e:
            raise Exception("Couldn't load Image. Exiting...")

        self.img_width, self.img_height = self.img.size

    def _set_font(self, font: Font = Font.IMPACT, size: int = None):
        """
        Set the internal ImageFont object

        :param font A Font enum
        :param size The font size
        """

        if not size:
            size = int(self.img_height / 10)

        try:
            self.font = ImageFont.truetype(font=str(font), size=size)
        except OSError:
            raise Exception("Couldn't load Font. Exiting...")

        self.char_width, self.char_height = self.font.getsize("A")

    def _make_image_draw(self):
        """
        Make the ImageDraw object
        """

        self.draw = ImageDraw.Draw(self.img)

    def _prepare_text(self, top_text: str, bottom_text: str):
        """
        Using `textwarp` split the `top_text` and `bottom_text` into lines
        so they can fit nicely on the image

        :param top_text The text to appear on top
        :param bottom_text The text to appear on bottom
        """

        top_text = top_text.upper()
        bottom_text = bottom_text.upper()

        max_chars_on_line = self.img_width // self.char_width

        top = textwrap.wrap(top_text, width=max_chars_on_line)
        bottom = textwrap.wrap(bottom_text, width=max_chars_on_line)

        return top, bottom

    def _draw_lines(self, lines: [str], start_y: int):
        """
        Draw specified lines at the specified start Y location

        :param lines The lines of text to draw
        :param start_y The starting Y-coordinate
        """

        y = start_y

        for line in lines:
            line_width, line_height = self.font.getsize(line)
            x = (self.img_width - line_width) / 2
            self._draw_shadow(
                x, y, line, "black"
            )  # Add border around text so it can be seen on all backgrounds
            self.draw.text((x, y), line, fill="white", font=self.font)
            y += line_height

    def _draw_shadow(
        self, x: int, y: int, line: str, border_color: ImageDraw.ImageColor
    ):
        """
        Draw shadow for text to be visible on all templates
        
        :param x The X-coordinate
        :param y The Y-coordinate
        :param line The text to draw
        :param border_color The color for the border
        """

        self.draw.text((x - 1, y - 1), line, font=self.font, fill=border_color)
        self.draw.text((x + 1, y - 1), line, font=self.font, fill=border_color)
        self.draw.text((x - 1, y + 1), line, font=self.font, fill=border_color)
        self.draw.text((x + 1, y + 1), line, font=self.font, fill=border_color)

        self.draw.text((x - 1, y - 1), line, font=self.font, fill=border_color)
        self.draw.text((x + 1, y - 1), line, font=self.font, fill=border_color)
        self.draw.text((x - 1, y + 1), line, font=self.font, fill=border_color)
        self.draw.text((x + 1, y + 1), line, font=self.font, fill=border_color)

    def write_text(self, top_text: str, bottom_text: str):
        """
        Add the classic TOP TEXT and BOTTOM TEXT of a meme template

        :param top_text Text to appear on top of meme
        :param bottom_text Text to appear on bottom of meme
        """

        top, bottom = self._prepare_text(top_text, bottom_text)
        y = 0
        self._draw_lines(top, y)

        y = self.img_height - self.char_height * len(bottom) - 10
        self._draw_lines(bottom, y)
