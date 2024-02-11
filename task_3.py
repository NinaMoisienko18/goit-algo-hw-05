def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            error_messages = {
                KeyError: "Contact not found.",
                ValueError: "Invalid input.",
                IndexError: "Invalid input. Please provide the name."
            }
            return error_messages.get(type(e), "An error occurred.")

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' changed."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"Phone number for {name}: {contacts[name]}"



@input_error
def show_all(contacts):
    if not contacts:
        return "There are no contacts."

    result = "\n>>> All Contacts:\n"
    for name, number in contacts.items():
        result += f"{name}: {number}\n"

    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
