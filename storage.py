from directory import contacts

def load_contacts():
    file = open("contacts.txt", "a+")
    file.seek(0)

    
    for line in file:
        data = line.strip().split(",")

    
    if len(data) == 2:
            contacts[data[0]] = data[1]
    file.close()

def save_contacts():
    file = open("contacts.txt", "w")

    for name, phone in contacts.items():
        file.write(name + "," + phone + "\n")
    file.close()
