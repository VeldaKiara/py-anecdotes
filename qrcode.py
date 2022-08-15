#dependencies intall pypng to access png
import pyqrcode
import png 
link = "https://github.com/VeldaKiara"
qr_code = pyqrcode.create(link)
qr_code.png("qrimage.png", scale=6)


