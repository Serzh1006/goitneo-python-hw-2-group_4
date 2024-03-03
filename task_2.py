def add_contact(args,contacts):
    try:
        name,phone = args
        contacts[name.lower()] = phone
        return "Contact added."
    except ValueError:
        return 'ValueError: not enough values to unpack (expected 2, got 0)'


def change_contact(args,contacts):
    try:
        name,phone = args
        for key in contacts:
            if key==name.lower():
                contacts[key] = phone
                return "Contact updated."
            else:continue
    except ValueError:
        return 'ValueError: not enough values to unpack (expected 2, got 0)'
    return 'Name is not found!'

def show_phone(args,contacts):
    try:
        name = args
        name = ("".join(name)).lower()
        for key in contacts:
            if key==name:
                return contacts[key]
            else: continue
    except ValueError:
        return 'ValueError: not enough values to unpack (expected 2, got 0)'
    return 'Name is not found!'


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