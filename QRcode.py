# Import the required modules
import qrcode
import cv2 as cv
from qrcode import constants

def Generate_qrcodes():
    """This function describes how we can generate qrcodes using QRcode available in qrcode module"""
    qr = qrcode.QRCode(version=1,error_correction=constants.ERROR_CORRECT_L,box_size=10,border=4)
    qr.add_data(f"Go To --> {'https://pypi.org/project/qrcode/'}")
    qr.make(fit=True)

    images = qr.make_image(fill_color='black',back_color='white')
    images.save('Images/pypi_qrcode.jpg')

if __name__ == "__main__":

    Generate_qrcodes()

    print("Code Completed 🔥")