import argparse
import sqlite3
# Eingaben
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
# Abfragen
parser.add_argument("--update", action="store_true", help="hinzufügen")
parser.add_argument("--delete", action="store_true", help="etwas löschen")
parser.add_argument("--get", action="store_true", help="?", )
parser.add_argument("--full", action="store_true", help="Gibt die Datenbank aus")
parser.add_argument("--names", action="store_true", help="Gibt die Id´s der Personen aus")
parser.add_argument("--field", action="store_true", help="Gibt ein beszimmten wert aus")

args = parser.parse_args()


class Adressen:
    def __init__(self,args):
        self.args = args
        self.firstname = args.firstname
        self.lastname = args.lastname
        self.street = args.street
        self.number = args.number
        self.postal_code = args.postal_code
        self.place = args.place
        self.brithday = args.birthday
        self.landline = args.landline
        self.mobile = args.mobile
        self.mail = args.mail

        self.insert_list = [args.firstname, args.lastname, args.birthday, args.street,
                            args.number, args.postal_code, args.place, args.landline, args.mobile, args.mail]


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
    info.insert_list.insert(0, "ALTER")

elif a_info.delete:
    info.insert_list.insert(0, "DELETE")

elif a_info.get:
    pass

elif a_info.full:
    pass

elif a_info.names:
    pass

elif a_info.field:
    pass

else:
    info.insert_list.insert(0, "INSERT")

print(info.insert_list)
print(info.insert_list[0], info.insert_list[1], info.insert_list[2], info.insert_list[3])


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
        #self.cursor.executemany(""" REPLACE INTO Adressen(Id, Firstname,Lastname,Birthday,Street)
        # VALUES(?,?,?,?,?,?,?,?,?,?,?)""", many_new_data)

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
