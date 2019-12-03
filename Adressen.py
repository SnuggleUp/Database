import argparse
import sqlite3
# Eingaben
parser = argparse.ArgumentParser()
adressen = parser.add_argument_group(title="Adressierungs Befehle")
aufgaben = parser.add_mutually_exclusive_group()
ausgaben = parser.add_argument_group(title="Ausgabe Befehle")
# Adressierungen
adressen.add_argument("--firstname", help="Vorname",)
adressen.add_argument("--lastname", help="Nachname",)
adressen.add_argument("--street", help="Staße",)
adressen.add_argument("--number", help="Hausnumemr",)
adressen.add_argument("--postal-code", help="Postleitzahl", type=int)
adressen.add_argument("--place", help="Ort",)
adressen.add_argument("--birthday", help="Das Geburtsdatum in YY-MM-DD",)
adressen.add_argument("--landline", help="Festnetznummer",)
adressen.add_argument("--mobile", help="Handynummer",)
adressen.add_argument("--mail", help="E-Mail",)
# Aufgaben
aufgaben.add_argument("--update", action="store_true", help="hinzufügen")
aufgaben.add_argument("--delete", action="store_true", help="etwas löschen")
aufgaben.add_argument("--search", action="store_true", help="Suchen")
aufgaben.add_argument("--get", action="store_true", help="?", )
# Ausgaben
ausgaben.add_argument("--full", action="store_true", help="Gibt die Datenbank aus")
ausgaben.add_argument("--names", action="store_true", help="Gibt die Id´s der Personen aus")
ausgaben.add_argument("--field", action="store_true", help="Gibt ein beszimmten wert aus")

args = parser.parse_args()


class Adressen:
    def __init__(self, args):

        self.action_dic = {"firstname": args.firstname, "lastname": args.lastname,"birthday": args.birthday,
                           "street": args.street, "number": args.number,"postal_code": args.postal_code,
                           "place": args.place, "landlline": args.landline,"mobile": args.mobile, "mail": args.mail}


class Abfragen:
    def __init__(self, args):
        self.args = args
        self.full = args.full
        self.names = args.names
        self.field = args.field
        self.search = args.search


        self.update = args.update
        self.delete = args.delete
        self.get = args.get



a_info = Abfragen(args)
info = Adressen(args)
if a_info.update:
    info.action_dic["sql_info"] = "ALTER"

elif a_info.delete:
    info.action_dic["sql_info"] = "DELETE"

elif a_info.get:
    pass

elif a_info.full:
    pass

elif a_info.names:
    pass

elif a_info.field:
    pass

else:
    info.action_dic["sql_info"] = "INSERT"

print(info.action_dic)
print(info.action_dic["lastname"],)

class AddressDatabase:

    def __enter__(self):
        return self

    def __del__(self):
        self.__db_connection.close()

    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect("Adressen.db")
        self.cur = self.connection.cursor()

    def __exit__(self):
        self.cursor.close()


    def execute(self, new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cur.execute(""" INSERT INTO Adressen(Id, Firstname,Lastname,Birthday,Street,Number,Postalcode,
                                Place,Landline,Mobile,Mail) VALUES(?,?,?,?,?,?,?,?,?,?,?,?);""", new_data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Adressen (Id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        self.connection.commit()