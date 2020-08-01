from enum import Enum


class MemeTemplate(Enum):
    FRY_SUSPICIOUS = "image_templates/futurama_fry_suspicious.png"

    def __str__(self):
        return str(self.value)
