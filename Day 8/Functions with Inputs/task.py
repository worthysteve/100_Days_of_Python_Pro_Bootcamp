def greet(name):
    print(f"Hello {name}!")
    print(f"How are you {name}?")
    print(f"Goodbye {name}!\n")

greet("Steven")

def greet_with_name(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with_name("Steven", "Washington")
greet_with_name(location = "Ankara", name = "Fenty")