import random
# # import my_module
from my_module import my_favorite_number

random_integer = random.randint(1, 10)
print(random_integer)

# print(my_module.my_favorite_number)
print(my_favorite_number)

# random number
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)


# random floating point number
random_floating_number = random.uniform(1, 10)
print(random_floating_number)

# Exercise
number = random.randint(1, 3)

if number == 1:
    print("Heads")
else:
    print("Tails")