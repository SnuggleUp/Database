import argparse
import sqlite3

# Eingaben
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
parser.add_argument("--delete", action="store_true", help="etwas löschen")
parser.add_argument("--get", action="store_true", help="?", )
parser.add_argument("--full", action="store_true", help="Gibt die Datenbank aus")
parser.add_argument("--names", action="store_true", help="Gibt die Id´s der Personen aus")
parser.add_argument("--field", action="store_true", help="Gibt ein beszimmten wert aus")

args = parser.parse_args()


class Adressen:
    def __init__(self, args):

        self.action_dic = {"firstname": args.firstname, "lastname": args.lastname,"birthday": args.birthday,
                           "street": args.street, "number": args.number,"postal_code": args.postal_code,
                           "place": args.place, "landlline": args.landline,"mobile": args.mobile, "mail": args.mail}


class Abfragen:
    def __init__(self, args):
        self.args = args
        self.update = args.update
        self.delete = args.delete
        self.get = args.get
        self.full = args.full
        self.names = args.names
        self.field = args.field


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
        self.connection.close()

    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect("Adressen.db")
        self.cursor = self.connection.cursor()

    def __exit__(self):
        self.cursor.close()

    def execute(self, new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cursor.execute(""" INSERT INTO Adressen(Id, Firstname,Lastname,Birthday,Street,Number,Postalcode,
                                Place,Landline,Mobile,Mail) VALUES(0,?,?,?,?,?,?,?,?,?,?);""", new_data)

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

AddressDatabase = AddressDatabase()
AddressDatabase.create_table()

print(AddressDatabase.commit())



