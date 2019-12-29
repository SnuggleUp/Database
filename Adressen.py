import argparse
import sqlite3
import itertools

# Eingabe
parser = argparse.ArgumentParser()
parser.add_argument("--firstname", help="Vorname", )
parser.add_argument("--lastname", help="Nachname", )
parser.add_argument("--street", help="Staße", )
parser.add_argument("--number", help="Hausnumemr", )
parser.add_argument("--postal-code", help="Postleitzahl", type=int)
parser.add_argument("--place", help="Ort", )
parser.add_argument("--birthday", help="Das Geburtsdatum in YY-MM-DD", )
parser.add_argument("--landline", help="Festnetznummer", )
parser.add_argument("--mobile", help="Handynummer", )
parser.add_argument("--mail", help="E-Mail", )
# Abfragen
parser.add_argument("--update", action="store_true", help="hinzufügen")
parser.add_argument("--delete", help="etwas löschen", )
parser.add_argument("--get", action="store_true", help="?", )
parser.add_argument("--full", action="store_true", help="Gibt die eine ganze zeile aus")
parser.add_argument("--names", action="store_true", help="Gibt die Id´s der Personen aus")
parser.add_argument("--field", action="store_true", help="Gibt ein beszimmten wert aus")
parser.add_argument("--list", action="store_true", help="Gibt die Datenbank aus ")
args = parser.parse_args()


class Adressen:
    def __init__(self, args):
        self.action_tub = (args.firstname, args.lastname, args.birthday, args.street, args.number, args.postal_code,
                           args.place, args.landline, args.mobile, args.mail)

        self.action_dic = {"firstname": args.firstname, "lastname": args.lastname, "birthday": args.birthday,
                           "street": args.street, "number": args.number, "postal_code": args.postal_code,
                           "place": args.place, "landlline": args.landline, "mobile": args.mobile, "mail": args.mail}


class Abfragen:
    def __init__(self, args):
        self.args = args
        self.update = args.update
        self.delete = args.delete
        self.get = args.get
        self.full = args.full
        self.names = args.names
        self.field = args.field

test = Abfragen(args)  
info = Adressen(args)

print(test.delete)


# print(info.action_tub)
# print(info.action_dic["lastname"], )
# ToDo
# Multible inserts bearbeiten
# 

class AddressDatabase:

    def __del__(self):
        self.connection.close()

    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect("Address.db", isolation_level=None)
        self.cursor = self.connection.cursor()

    def __exit__(self):
        self.cursor.close()

    def __add__(self, other):
        pass

    def execute(self, data):
        """add new data to database in one go"""
        self.create_table()
        self.cursor.execute(""" INSERT INTO Adressen(Id, Firstname,Lastname,Birthday,Street,Number,Postalcode,
                                Place,Landline,Mobile,Mail) VALUES(NULL,?,?,?,?,?,?,
                                ?,?,?,?);""", data)
        print(data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Adressen (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                             Firstname VARCHAR (50),
                                             Lastname VARCHAR(50),
                                             Birthday Varchar(50),
                                             Street VARCHAR (50),
                                             Number VARCHAR(50),
                                             Postalcode VARCHAR(50),
                                             Place VARCHAR(50),
                                             Landline VARCHAR (50),
                                             Mobile VARCHAR(50),
                                             Mail VARCHAR(50)); """)

    def commit(self):
        self.connection.commit()

    def delete(self, data):
        self.cursor.execute(""" DELETE FROM Adressen WHERE Id = ? """, data)

    def update(self):
        self.cursor.execute("""UPDATE Adressen SET ? = ? WHERE Id = ? """)

    def search(self):
        self.cursor.execute("""SELECT ? FROM Adressen""")

    def get(self):
        self.cursor.execute("""SELECT Id, firstname, lastname FROM Adressen""")

    def full(self):
        self.cursor.execute("""SELECT * FROM Adressen""")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def select(self, data):
        self.cursor.execute("""SELECT * FROM Adressen where Id = ? """.replace("?",data[0]), data)


AddressDatabase = AddressDatabase()
AddressDatabase.create_table()
if info.action_tub[0] and info.action_tub[1] and len(
        tuple(itertools.filterfalse(None, info.action_tub))) < 8:
    AddressDatabase.execute(data=info.action_tub)
else:
    print("Sie müssen Vorname, Nachname und ein weiteres Attribut angeben")

if test.delete is not None:
    AddressDatabase.delete(data=test.delete)

if test.full is True:
    AddressDatabase.full()
