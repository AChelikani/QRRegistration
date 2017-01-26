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
        self.makeQR(self.createContents(id), 6, "qr/" + str(id)+".png")

    # File with just id number in each line
    def createQRFromFile(self, filename):
        with open(filename, 'r') as f:
            text = f.readlines()
            for line in text:
                entry = int(line.rstrip())
                self.createQR(entry)


if __name__ == "__main__":
    qr = QRCodeCreator()
    qr.createQR(1)
