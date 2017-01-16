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

        self.dbname = dbname

    def validate(self):
        uniqueID = clipboard.paste()
        print uniqueID
        res = self.inDatabase(uniqueID)
        if (res["error"]):
            print res["msg"]
            playsound("sounds/no.mp3")
        else:
            print res["msg"]
            playsound("sounds/hello.mp3")

    def inDatabase(self, ID):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute('SELECT * FROM attendees WHERE id=(?)', (ID,))
        res = c.fetchone()
        print res
        if (res is None):
            conn.close()
            return {"error" : True, "msg" : "Not in database"}
        elif (res[3] == 1):
            return {"error" : True, "msg" : "Already checked in"}
        else:
            c.execute('UPDATE attendees SET checkedin=1 WHERE id=?', ID)
            conn.commit()
            conn.close()
            return {"error" : False, "msg" : "Welcome"}
        return {"error" : True, "msg" : "None"}


if __name__ == "__main__":
    root = Tk()
    app = App(root, "participants.db")
    root.mainloop()
