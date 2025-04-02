from random import choice, randint

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

bill_paid_by = choice(friends)
print(bill_paid_by)

# 2nd Option
random_index = randint(0, 4)
print(friends[random_index])

