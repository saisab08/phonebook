import csv

csv_file = 'phone.csv'

class ContactDetails:
    def __init__ (self, name, phone_no, email):
        self.name = name
        self.phone_no = phone_no
        self.email = email

    def addContact(self):
        print("Enter the details below")
        self.name = input("Name: ")
        self.phone_no = input("Phone Number: ")
        self.email = input("Email: ")

        with open(csv_file, 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.phone_no, self.email])

    def viewContacts(self):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for contact in reader:
                if(len(contact) == 0):
                    continue
                print(contact)

    def deleteContact(self):
        email = input("Enter email of the contact to delete: ")
        contacts_to_keep = []

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for contact in reader:
                if len(contact) == 0 or contact[2] == email:
                    continue
                contacts_to_keep.append(contact)

        with open(csv_file, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(contacts_to_keep)

    def updateContact(self):
        email = input("Enter email of the contact to update: ")
        contacts_to_write = []

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for contact in reader:
                if len(contact) == 0:
                    continue
                elif contact[2] == email:
                    name = input("Updated Name: ")
                    phone_no = input("Updated Phone No: ")
                    new_email = input("Updated Email: ")
                    updated_contact = [name, phone_no, new_email]
                    contacts_to_write.append(updated_contact)
                else:
                    contacts_to_write.append(contact)

        with open(csv_file, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(contacts_to_write)