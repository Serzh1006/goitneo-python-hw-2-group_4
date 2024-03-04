def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Key error. The contact not found."
        except IndexError:
            return "Index error. Try again."
    return inner


@input_error
def add_contact(args,contacts):
        name,phone = args
        contacts[name.lower()] = phone
        return "Contact added."

@input_error
def change_contact(args,contacts):
        name,phone = args
        for key in contacts:
            if key==name.lower():
                contacts[key] = phone
                return "Contact updated."
            else:continue
        return contacts[name]

@input_error
def show_phone(args,contacts):
        name = args
        name = ("".join(name)).lower()
        for key in contacts:
            if key==name:
                return contacts[key]
            else: continue
        return contacts[name]


def show_all(contacts):
    if len(contacts)==0:
        print('List is empty!')
    for key,value in contacts.items():
        print(f'{key.capitalize()}: {value}')


def parce_input(user_input):
    cmd,*args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd,*args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input('Enter a command: ')
        command,*args = parce_input(user_input)
        if command in ['close','exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args,contacts))
        elif command == 'change':
            print(change_contact(args,contacts))
        elif command == 'phone':
            print(show_phone(args,contacts))
        elif command == 'all':
            show_all(contacts)
        else: print('Invalid command.')

if __name__ == "__main__":
    main()