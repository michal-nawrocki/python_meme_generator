from PIL import (
    Image,
    ImageDraw,
    ImageFilter,
    ImageFont,
)
import sys


def main():

    image = Image.open("image_templates/futurama_fry_suspicious.png")
    font = ImageFont.truetype("fonts/impact.ttf")

    image.show()

    draw = ImageDraw.Draw(image)

    draw.text((0, 0), "TEST 123", (255, 255, 255), font=font)
    image.show()

if __name__ == "__main__":
    main()
