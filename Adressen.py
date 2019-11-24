import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument("--firstname", help="Vorname",)
parser.add_argument("--lastname", help="Nachname",)
parser.add_argument("--street", help="Staße",)
parser.add_argument("--number", help="Hausnumemr",)
parser.add_argument("--postal-code", help="Postleitzahl", type=int)
parser.add_argument("--place", help="Ort",)
parser.add_argument("--birthday", help="Das Geburtsdatum in YY-MM-DD",)
parser.add_argument("--landline", help="Festnetznummer",)
parser.add_argument("--mobile", help="Handynummer",)
parser.add_argument("--mail", help="E-Mail",)
# Ausgaben
parser.add_argument("--get", help="?")
parser.add_argument("--full", help="Gibt die Datenbank aus",)
parser.add_argument("--names", help="Gibt die Id´s der Personen aus")
parser.add_argument("--field", help="Gibt ein beszimmten wert aus")

args = parser.parse_args()


class Adressen:
    def __init__(self,args):
        self.args = args
        self.firstname = args.firstname
        self.lastname = args.lastname
        self.street = args.street
        self.number = args.number
        self.place = args.place
        self.brithday = args.birthday
        self.landline = args.landline
        self.mobile = args.mobile
        self.mail = args.mail
info = Adressen(args)
print(info.firstname)

class AddressDatabase:

    def __enter__(self):
        return self

    def __init__(self):
        self.sqlcon = sqlite3.connect("Adressen.db")
        self.cursor = self.sqlcon.cursor()

    def close(self):
        self.sqlcon.close()

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.sqlcon.rollback()
        else:
            self.sqlcon.commit()
            self.sqlcon.close()

    def execute(self, new_data):
        self.cursor.execute(new_data)

    def executemany(self, many_new_data):
        self.create_table()
        #self.cursor.executemany(""" REPLACE INTO Adressen(Id, Firstname,Lastname,Birthday,Street) VALUES(?,?,?,?,?,?,?,?,?,?,?)""", many_new_data)

    def create_table(self):
        self.cursor.execute("""CREATE TABLE if NOT EXISTS Adressen (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                             Firstname VARCHAR (50),
                                             Lastname VARCHAR(50),
                                             Birthday Varchar(50),
                                             Street VARCHAR (50),
                                             Number VARCHAR(50),
                                             Postalcode INTEGER,
                                             Place VARCHAR(50),
                                             Landline VARCHAR (50),
                                             Mobile VARCHAR(50),
                                             Mail VARCHAR(50)); """)
    def commit(self):
        self.sqlcon.commit()
#ToDo
