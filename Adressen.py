import argparse
import itertools
import sqlite3
import datetime

# Eingabe
parser = argparse.ArgumentParser()
parser.add_argument("--firstname", help="Vorname", )
parser.add_argument("--lastname", help="Nachname", )
parser.add_argument("--street", help="Staße", )
parser.add_argument("--number", help="Hausnumemr", )
parser.add_argument("--postal-code", "-PLZ", help="Postleitzahl", type=int)
parser.add_argument("--place", help="Ort", )
parser.add_argument("--birthday", help="Das Geburtsdatum in YYYY-MM-DD", )
parser.add_argument("--landline", help="Festnetznummer", )
parser.add_argument("--mobile", help="Handynummer", )
parser.add_argument("--mail", help="E-Mail", )
# Abfragen
parser.add_argument("--update", action="store_true", help="hinzufügen")
parser.add_argument("--delete", "-del", help="etwas löschen", )
parser.add_argument("--get", help="Gibt zu einer ID den Vornamen und Nachnamen aus ", type=int)
parser.add_argument("--full", action="store_true", help="Gibt die eine ganze zeile aus")
parser.add_argument("--names", action="store_true", help="Gibt die Id´s der Personen aus")
parser.add_argument("--field", help="Gibt ein beszimmten wert aus")
parser.add_argument("--list", action="store_true", help="Gibt die Datenbank aus ")
parser.add_argument("--search", action="store_true", help="Bestimmte Sachen suchen ")
parser.add_argument("--today", action="store_true", help="Gibt an wer heute Geburtstag hat")
args = parser.parse_args()

# print(info.action_tub)
# print(info.action_dic["lastname"], )
# ToDo
# Multible inserts bearbeiten


class AddressDatabase:

    def __del__(self):
        """Closes the connection to the db"""
        self.connection.close()

    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect("Address.db", isolation_level=None)
        self.cursor = self.connection.cursor()

    def __exit__(self):
        """Closes the cursor"""
        self.cursor.close()

    def __add__(self, other):
        pass


    def create_table(self):
        """create a database table if it does not exist already"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Adressen (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                             Firstname VARCHAR (50),
                                             Lastname VARCHAR(50),
                                             Birthday DATE ,
                                             Street VARCHAR (50),
                                             Number VARCHAR(50),
                                             Postalcode VARCHAR(50),
                                             Place VARCHAR(50),
                                             Landline VARCHAR (50),
                                             Mobile VARCHAR(50),
                                             Mail VARCHAR(50)); """)


    def insert(self, data):
        """adds the values in the table Adressen"""
        self.create_table()
        self.cursor.execute(""" INSERT INTO Adressen(Id, Firstname,Lastname,Birthday,Street,Number,Postalcode,
                                Place,Landline,Mobile,Mail) VALUES(NULL,?,?,?,?,?,?,
                                ?,?,?,?);""", data)


    def get_name(self, data):
        """Prints the names and the id"""
        self.cursor.execute("""SELECT Id, firstname, lastname FROM Adressen WHERE Id = ?""", data)
        row = self.cursor.fetchall()
        id_info = row[0]
        print(id_info[0], id_info[1], id_info[2])

    def get_full(self, data):
        """prints the hole line from one Id"""
        self.cursor.execute("""SELECT * FROM Adressen where Id = ? """,data)
        row = self.cursor.fetchall()
        id_info = row[0]
        print("Id:", id_info[0],
              "Firstname:", id_info[1],
              "Lastname:", id_info[2],
              "Birthday:", id_info[3],
              "Street:", id_info[4],
              "Number:", id_info[5],
              "Postalcode:", id_info[6],
              "Place:", id_info[7],
              "Landline:", id_info[8],
              "Mobile:", id_info[9],
              "Mail:", id_info[10])

    def get_field(self, data):
        """This Program outputs the requestet values"""
        self.cursor.execute("SELECT ~ FROM Adressen WHERE Id = ?".replace("~", data[0]), data[1])
        row = self.cursor.fetchall()
        print(row[0])

    def names(self, data):
        """Is nearly the same as get_names but with like and its ordered"""
        self.cursor.execute("SELECT Id, Firstname, Lastname FROM Adressen "
                            "WHERE firstname LIKE ? AND lastname LIKE ? AND street LIKE ? "
                            "AND number LIKE ? AND postalcode LIKE ? AND place LIKE ? AND birthday LIKE ? "
                            "AND landline LIKE ? AND mobile LIKE ? AND mail LIKE ? "
                            "ORDER BY lastname,firstname DESC", data)
        row = self.cursor.fetchall()
        print(row)

    def field(self, data):
        print(data)
        """Is nearly the same as get_field but with like and its ordered"""
        self.cursor.execute("SELECT ~ FROM Adressen WHERE firstname LIKE ? AND lastname LIKE ? AND street LIKE ? "
                    "AND number LIKE ? AND postalcode LIKE ? AND place LIKE ? AND birthday LIKE ? "
                    "AND landline LIKE ? AND mobile LIKE ? AND mail LIKE ? "
                    "ORDER BY lastname,firstname DESC".replace("~",data[1]),data[0])
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def full(self, data):
        """Is nearly the same as get_full but with like and its ordered"""
        self.cursor.execute("SELECT * FROM Adressen WHERE firstname LIKE ? AND lastname LIKE ? AND street LIKE ? "
                     "AND number LIKE ? AND postalcode LIKE ? AND place LIKE ? AND birthday LIKE ? "
                     "AND landline LIKE ? AND mobile LIKE ? AND mail LIKE ? "
                     "ORDER BY lastname,firstname DESC", data)
        row = self.cursor.fetchall()
        print(row)

    def delete(self, data):
        """Delets the line with the Id"""
        self.cursor.execute(""" DELETE FROM Adressen WHERE Id = ? """, data)

    def update(self, data):
        """Updates the table"""
        self.cursor.execute("""UPDATE Adressen SET ~ = ? WHERE Id = ? """.replace("~",data[3]),data)

    def search(self, data):
        """Searches for a line"""
        self.cursor.execute("""SELECT ? FROM Adressen WHERE Id = ?""".replace("?",data[0]),data )

    def list(self):
        """Outputs the whole Database"""
        self.cursor.execute("""SELECT * FROM Adressen""")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


AddressDatabase = AddressDatabase()
AddressDatabase.create_table()

class Adressen:
    def __init__(self, args):

        self.action_list = (args.firstname, args.lastname, args.birthday, args.street, args.number, args.postal_code,
                           args.place, args.landline, args.mobile, args.mail)
        self.action_tup = []
        for element in self.action_list:
            if element is None:
                element = "/"
                self.action_tup.append(element)
            else:
                self.action_tup.append(element)

        # insert
        if self.action_tup[0] and self.action_tup[1] and len(
                tuple(itertools.filterfalse(None, self.action_tup))) < 8:
            AddressDatabase.insert(data=self.action_tup)
        elif self.action_tup[0] and self.action_tup[1] and len(
                tuple(itertools.filterfalse(None, self.action_tup))) < 9:
            print("Sie müssen Vorname, Nachname und ein weiteres Attribut angeben")



class Abfragen:
    def __init__(self, args):
        self.args = args
        self.update = args.update
        self.delete = args.delete
        self.get = args.get
        self.full = args.full
        self.names = args.names
        self.field = args.field
        self.list = args.list
        self.search = args.search
        self.today = args.today
        self.action_list = [args.firstname, args.lastname, args.birthday, args.street, args.number, args.postal_code,
                           args.place, args.landline, args.mobile, args.mail]
        # Delete
        if self.delete:
            AddressDatabase.delete(data=([self.delete]))
        # complete database
        if self.list is True:
            AddressDatabase.list()
        # get
        if self.get and self.full is False and self.field is None:
            AddressDatabase.get_name(data=([self.get]))

        if self.get and self.full:
            AddressDatabase.get_full(data=([self.get]))

        if self.get and self.field:
            AddressDatabase.get_field(data=(self.field, [self.get]))
        if self.search:
            self.info = []
            for element in self.action_list:
                if element:
                    element = str(element).replace("*", "%")
                    self.info.append(element)
                else:
                    self.info.append("%")

            AddressDatabase.full(data=(self.info))
        if self.search and self.field:

            AddressDatabase.field(data=(self.info, self.field))





Adressen(args)
Abfragen(args)

