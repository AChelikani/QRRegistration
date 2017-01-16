import pyqrcode

qr = pyqrcode.create("Test")
qr.png("test.png", scale=6)

class QRCode(object):
    def __init__(self, id):
        self.id = id

    def makeQR(self, contents, scale, filename):
        qr = pyqrcode.create(contents)
        qr.png(filename, scale=scale)

    def createContents(self):
        return self.id

    def createQR(self):
        self.makeQR(createContents(), 6, str(self.id)+".png")

if __name__ == "__main__":
    pass
