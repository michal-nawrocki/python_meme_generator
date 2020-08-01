from font import Font
from meme import Meme
from meme_template import MemeTemplate


def main():

    meme = Meme(MemeTemplate.FRY_SUSPICIOUS)
    meme.set_font(Font.IMPACT, 20)
    meme.img.show()


if __name__ == "__main__":
    main()
