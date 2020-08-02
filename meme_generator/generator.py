from font import Font
from meme import Meme
from meme_template import MemeTemplate


def main():

    meme = Meme(MemeTemplate.FRY_SUSPICIOUS, Font.COMIC_SANS)
    meme.write_text("Clicks Run", "Compiler doesn't complain")
    meme.img.show()


if __name__ == "__main__":
    main()
