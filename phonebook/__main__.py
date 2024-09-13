from phone import ContactDetails

def menu():
    print("Choose any action from the given list")
    print("-"*25)
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("0. Exit")
    print("-"*25)

def run():
    menu()
    choice = int(input("Choice: "))

    if choice != 0:
        if choice == 1:
            c1 = ContactDetails('','','')
            c1.addContact()
        elif choice == 2:
            c1 = ContactDetails('','','')
            c1.viewContacts()
        elif choice == 3:
            c1 = ContactDetails('','','')
            c1.deleteContact()
        elif choice == 4:
            c1 = ContactDetails('','','')
            c1.updateContact()
        else:
            print("Invalid Choice")
        run()
    else:
        print("Program Exited")

if __name__ == '__main__':
    run()