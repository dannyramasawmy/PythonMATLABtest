def repeatText(number : float, text : str):
    """ returns a string <text> repeated <number> times"""
    return int(number) * text

def countLetters(text : str):
    """ returns a dictionary of the letters in text counted"""
    return {letter : text.count(letter) for letter in set(text)}


class PhoneBook():
    def __init__(self):
        self.contacts = set()
        self.hash = set()
        
    def add(self, name : str, number : str):
        contact = Contact(name, number)
        if contact.uniqueID not in self.hash:
            self.contacts.add(contact)
            self.hash.add(contact.uniqueID)

    def ring(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f'{contact.name}..Ring ring..')
                break

    def __repr__(self):
        return ' | '.join([str(contact) for contact in self.contacts])


class Contact():
    def __init__(self, name : str, number: str):
        self.name = name
        self.number = number 

    def __repr__(self):
        return f'{self.name} at {self.number}'

    def __hash__(self):
        return hash(repr(self))

    @property
    def uniqueID(self):
        return self.__hash__()



if __name__ == "__main__":
    
    # test repeat character
    print(f"{repeatText(50, 'a')}")

    # test count letters
    print(f"{countLetters('the quick brown fox jumped over the lazy and dog')}")

    # quick phone book example
    myPB = PhoneBook()
    myPB.add('John', '0123456')
    myPB.add('Jane', '0133156')
    myPB.add('Jo', '0126456')
    myPB.add('Jo', '0126456')
    myPB.add('Jo', '0123333')
    print(myPB)    
    myPB.ring('Jo')

