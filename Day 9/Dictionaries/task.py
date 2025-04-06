programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary["Loop"] = "The action of doing something over and over again."


empty_dictionary = {}

print(programming_dictionary["Bug"])

print(programming_dictionary)

# wipe existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

for key, value in programming_dictionary.items():
    print(f"A {key} is {value}")