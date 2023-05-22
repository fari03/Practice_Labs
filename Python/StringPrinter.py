class StringPrinter:
    def __init__(self):
        pass

    def accept_string(self):
        self.user_string = input("Enter a string: ")

    def print_string(self):
        print("User string:", self.user_string)

# Example usage
printer = StringPrinter()

printer.accept_string()
printer.print_string()
