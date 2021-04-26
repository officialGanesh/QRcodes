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


def Decode_data():
    """The above fuction can decode the data hidden in qrcodes"""
    image = cv.imread('Images/pypi_qrcode.jpg')
    Qr_Code_Generator = cv.QRCodeDetector()
    retVal ,point, stQr = Qr_Code_Generator.detectAndDecode(image)
    print(retVal)

if __name__ == "__main__":
    Generate_qrcodes()
    Decode_data()

    print("Code Completed 🔥")