def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
print(format_name(input("What is your first name? "), input("What is your last name? ")))

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False

print(canBuyAlcohol(17))

# Empty Returns
# You can also write return without anything afterwards, and this just tells the function to exit.
#
# e.g.

def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False

print(canBuyAlcohol(17.0))