import os
import qrcode

from PIL.Image import open
from PIL.Image import Image 
from qrcode.constants import ERROR_CORRECT_H

class QRGenerator:
    def __init__(self, data: str, fill: str= "white", back: str="black", size: int=10, img: Image | None=None) -> None:
       self.data: str = data
       self.fill: str = fill
       self.back: str = back
       self.size: int = size
       self.img: Image | None = img

    def generate(self) -> Image:

        qr = qrcode.QRCode(
                version=1,
                error_correction=ERROR_CORRECT_H,
                box_size=self.size,
                border=4
                )
        qr.add_data(self.data)
        qr.make(fit=True)

        self.img = qr.make_image(
                fill_color = self.fill,
                back_color = self.back
                ).get_image()

        return self.img

    def save_qr(self, name_file: str="qrcode", folder: str="outputs") -> str:
        if self.img is None:
             raise ValueError("QR code belum di generate!")

        if not os.path.exists(folder):
            os.makedirs(folder)

        path: str = f"{folder}/{name_file}.png"
        self.img.save(path)

        return path

    def add_logo(self, logo_path: str) -> None:
        if self.img is None:
            raise ValueError("QR belum di generate!")

        logo = open(logo_path)
        logo = logo.resize((100, 100))

        qr_width, qr_height = self.img.size
        logo_width, logo_height = logo.size

        X = (qr_width - logo_width) // 2
        y = (qr_height - logo_height) // 2

        self.img.paste(logo, (X, y), logo)
