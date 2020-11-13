def repeatText(number : float, text : str):
    """ returns a string repeated number times"""
    return int(number) * text

def countLetters(text : str):
    """ returns a dictionary of the letters in text counted"""
    return {letter : text.count(letter) for letter in set(text)}


class PhoneBook():
    def __init__(self):
        self.contacts = set()
        self.hash = set() # check contact is unique

    def add(self, name : str, number : str):
        contact = Contact(name, number)
        if contact.uniqueID not in self.hash:
            self.contacts.add(contact)
            self.hash.add(contact.uniqueID)

    def ring(self, name : str):
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

def fib(n):
    if n < 3:
        return 1
    
    a = 1
    b = 1
    
    for i in range(3, n+1):
        c = a + b
        b, a = c, b 
    
    return c 


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

    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    
    
    
