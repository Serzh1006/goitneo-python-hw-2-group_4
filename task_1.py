from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,new_phone):
        phone = Phone(new_phone)
        self.phones.append(phone.value)

    def remove_phone():
        pass


    def edit_phone(self,old,new):
        index = self.phones.index(old)
        self.phones[index] = new

    def find_phone():
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
       self.data[record.name.value] = record

    def find(self,name):
        return self.data[name]

    def delete(self,name):
        self.data.pop(name)

john_record = Record('John')
book = AddressBook()
alina_record = Record('Alina')
john_record.add_phone('733101770')
john_record.add_phone('1234567890')
alina_record.add_phone('794325346')
book.add_record(john_record)
book.add_record(alina_record)

john = book.find('John')
john.edit_phone('733101770','101010101010')
book.delete('John')
book.delete('Alina')
print(book.data)
