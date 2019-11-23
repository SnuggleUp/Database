import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument("--firstname", help="Vorname",)
parser.add_argument("--lastname", help="Nachname",)
parser.add_argument("--street", help="Staße",)
parser.add_argument("--number", help="Hausnumemr",)
parser.add_argument("--postal-code", help="Postleitzahl", type=int, metavar="ZIP")
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
#^^
class Adressen:
    def __init__(self, args):

        self.firstname = args.firstname
        self.lastname = args.lastname
        self.street = args.street
        self.number = args.number
        self.place = args.place
        self.brithday = args.birthday
        self.landline = args.landline
        self.mobile = args.mobile
        self.mail = args.mail

infos = Adressen(args)
print(infos.mobile)
class AddressDatabase():
    try:
        sqlcon = sqlite3.connect("Adressen.db")
        cursor = sqlcon.cursor()

        sqltable = """CREATE TABLE Adressen (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                             Firstname VARCHAR (50),
                                             Lastname VARCHAR(50),
                                             Birthday Varchar(50),
                                             Street VARCHAR (50),
                                             Number VARCHAR(50),
                                             Postalcode INTEGER,
                                             Place VARCHAR(50),
                                             Landline VARCHAR (50),
                                             Mobile VARCHAR(50),
                                             Mail VARCHAR(50));"""

        cursor.execute(sqltable)
        sqlcon.commit()
        print("SQLite table created")


    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    pass
#ToDo
