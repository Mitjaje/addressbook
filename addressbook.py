class Kontakt():
    def __init__(self, first_name, last_name, address, phone, email):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.phone=phone
        self.email=email
    def polni_kontakt(self):
        print "%s %s %s %s %s"% (self.first_name, self.last_name, self.address, self.phone, self.email)
addressbook=[]
while True :
    odgovor = raw_input("Dodaj kontakt?")
    if odgovor == 'da':
        first_name = raw_input("Ime: ")
        last_name = raw_input("Priimek: ")
        address=raw_input("Naslov: ")
        phone=raw_input("Telefon: ")
        email=raw_input("Email: ")
        nov_kontakt = Kontakt(first_name=first_name, last_name=last_name, address=address, phone=phone, email=email)
        addressbook.append(nov_kontakt)
    elif odgovor == 'ne':
        for kontakt in addressbook:
            kontakt.polni_kontakt()
        break
    else:
        print "Prosim odgovori z 'da' ali 'ne'"