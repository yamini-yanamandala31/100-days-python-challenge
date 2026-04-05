import qrcode

data = input("Enter text or link: ")

qr = qrcode.make(data)

qr.save("my_qr.png")

print("QR Code generated and saved as my_qr.png")
