from tkinter import *
import clipboard
import sqlite3


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
        if (self.inDatabase(uniqueID)):
            print "Found %s" %uniqueID
        else:
            print "Not Found!"

    def inDatabase(self, ID):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute('SELECT * FROM attendees WHERE id=?', ID)
        res = c.fetchone()
        if (res is None):
            conn.close()
            return False
        else:
            c.execute('UPDATE attendees SET checkedin=1 WHERE id=?', ID)
            conn.commit()
            conn.close()
            return True
        return False


if __name__ == "__main__":
    root = Tk()
    app = App(root, "participants.db")
    root.mainloop()
