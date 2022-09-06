# Qr code generator in python
import qrcode
# from PIL import Image
# from pyzbar.pyzbar import decode


# img= qr.make("https://www.nepsico.com")
# image.save("nepcico_com.png")

qr = qrcode.create("coding with omsah")
qr.png("mycode.png",scale=8)
