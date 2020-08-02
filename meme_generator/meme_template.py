from enum import Enum


class MemeTemplate(Enum):
    """
    Enum to get location of available meme template (i.e. image)
    """

    FRY_SUSPICIOUS = "../image_templates/futurama_fry_suspicious.png"

    def __str__(self):
        return str(self.value)
