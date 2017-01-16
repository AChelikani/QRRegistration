import pyqrcode

qr = pyqrcode.create("Test")
qr.png("test.png", scale=6)

class QRCode(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def makeQR(self, contents, scale, filename):
        qr = pyqrcode.create(contents)
        qr.png(filename, scale=scale)

    def createContents(self):
        return self.fname + " | " + self.lname

    def createQR(self):
        makeQR(createContents(), 6, fname+lname+".png")9
