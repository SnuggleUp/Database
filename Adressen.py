import argparse

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
args = parser.parse_args()

# Werte
firstname = args.firstname
lastname = args.lastname
street = args.street
number = args.number
place = args.place
birthday = args.birthday
landline = args.landline
mobile = args.mobile
mail = args.mail


print(firstname)
print(args)
print(mobile)

class Adressen:
    def __init__(self,firstname, lastname,
                 street, number, place,
                 birthday, landline, mobile,
                 mail):
        
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.number = number
        self.place = place
        self.brithday = birthday
        self.landline = landline
        self.mobile = mobile
        self.mail = mail

class AddressDatabase():
    pass
#ToDo
