import generator
import json

def main():
    contacts = []
    for _ in range(100):
        contact = generator.generate_contact()
        contacts.append(contact)
    
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)
        
if __name__ == "__main__":
    main()
        