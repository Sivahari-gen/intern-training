contacts ={}
class DigitError(Exception):
    pass
def add_contact():
    try:
        name = input("Enter name")
        phone = int(input("Enter phone number"))
        phone = str(phone)
        if len(phone)!= 10:
            raise DigitError
        contacts[name] = phone
        return print(f"{name} contact added")
    except DigitError as e:
        print("phone number must be have 10 digits")
    except ValueError as e:
        print("Enter valid data")
    # finally:
    #     if len(phone)!= 10:
    #         raise ValueError ("enter valid 10 digit phone number")
def find_contact():
    name = (input("Enter name to search"))
    try:
        if name in contacts:
            return print(name,":",contacts[name])
        else:
            raise ("not found")
    except NameError as e:
        print("NameError")
def list_contacts():
    print("\nContacts:")
    for name in contacts:
        return print(name,":",contacts[name])

# add_contact()
# add_contact()
# find_contact("siva")
# find_contact("sivahari")
# list_contacts()