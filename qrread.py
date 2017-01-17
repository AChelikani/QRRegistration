from tkinter import *
import clipboard
import sqlite3
from playsound import playsound

class App:
    def __init__(self, master, dbname):
        frame = Frame(master)
        frame.pack()
        self.quit = Button(frame, text="Quit", command=quit)
        self.quit.pack(side=LEFT)

        self.validate = Button(frame, text="Validate", command=self.validate)
        self.validate.pack(side=LEFT)

        self.manualText = Entry(master)
        self.manualText.pack(side=LEFT)

        self.manual = Button(frame, text="Manual", command=self.manual)
        self.manual.pack(side=LEFT)

        self.dbname = dbname

    def validateID(self, id):
        res = self.inDatabase(id)
        if (res["error"]):
            print res["msg"]
            playsound("sounds/no.mp3")
        else:
            print res["msg"]
            playsound("sounds/hello.mp3")

    def validate(self):
        uniqueID = clipboard.paste()
        res = self.validateID(uniqueID)

    def manual(self):
        text = self.manualText.get()
        if (text):
            self.validateID(int(text))

    def inDatabase(self, ID):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute('SELECT * FROM attendees WHERE id=(?)', (ID,))
        res = c.fetchone()
        if (res is None):
            conn.close()
            return {"error" : True, "msg" : "Not in database"}
        elif (res[4] == 1):
            return {"error" : True, "msg" : "Already checked in"}
        elif (res[3] == 0):
            return {"error" : True, "msg" : "Waiver not completed"}
        else:
            c.execute('UPDATE attendees SET checkedin=1 WHERE id=(?)', (ID,))
            conn.commit()
            conn.close()
            return {"error" : False, "msg" : "Welcome" + res[1] + res[2]}
        return {"error" : True, "msg" : "None"}


if __name__ == "__main__":
    root = Tk()
    app = App(root, "participants.db")
    root.mainloop()
