from faker import Faker
import re

fake = Faker()

def generate_name():
    found = False
    while not found:
        full_name = fake.name()
        name_list = full_name.split(" ")
        if len(name_list) == 2:
            found = True
    return name_list[0], name_list[1]

def generate_number():
    found = False
    while not found:
        number = fake.phone_number()
        pattern = re.compile("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]")
        result = re.fullmatch(pattern, number)
        if result:
            number = number[0:3] + number[4:7] + number[8:]
            found = True
    return number

def generate_email():
    return fake.email()
        
def generate_contact():
    contact = {}
    first_name, last_name = generate_name()
    number = generate_number()
    email = generate_email()
    contact["First Name"] = first_name
    contact["Last Name"] = last_name
    contact["Number"] = number
    contact["Email"] = email
    contact["Tags"] = []
    return contact