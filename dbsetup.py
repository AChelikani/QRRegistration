import sqlite3


class DBCreator(object):
    def __init__(self):
        pass

    def createFromFile(self, filename):
        conn = sqlite3.connect('participants.db')
        c = conn.cursor()
        c.execute('''DROP TABLE attendees''');
        c.execute('''CREATE TABLE attendees
             (id integer, fname text, lname text, email text, waiver integer, checkedin integer)''')
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                entry = line.rstrip().split(" ")
                print entry
                c.execute("INSERT INTO attendees VALUES (?, ?, ?, ?, ?, 0)", (entry[0], entry[1], entry[2], entry[3], int(entry[4])))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    dbCreator = DBCreator()
    dbCreator.createFromFile("sample.txt")
