from directory import contacts


def load_contacts():
    file = open("contacts.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if len(data) == 2:
            name = data[0]
            phone = data[1]
            contacts[name] = phone

    file.close()


def save_contacts():
    file = open("contacts.txt", "w")

    for name in contacts:
        phone = contacts[name]
        file.write(name + "," + phone + "\n")

    file.close()
