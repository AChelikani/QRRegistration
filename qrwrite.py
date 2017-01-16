import pyqrcode

qr = pyqrcode.create("Test")
qr.png("test.png", scale=6)

class QRCodeCreator(object):
    def __init__(self):
        pass

    def makeQR(self, contents, scale, filename):
        qr = pyqrcode.create(contents)
        qr.png(filename, scale=scale)

    def createContents(self, id):
        return id

    def createQR(self, id):
        self.makeQR(self.createContents(id), 6, str(id)+".png")

if __name__ == "__main__":
    qr = QRCodeCreator()
    qr.createQR(2)
