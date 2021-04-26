import pyqrcode
import png
def qrcode():
    q = pyqrcode.create(input("Enter Website:"))
    q.png('qrcode.png',scale=6)
    print("QR Generated")

if __name__=='__main__':
    qrcode()