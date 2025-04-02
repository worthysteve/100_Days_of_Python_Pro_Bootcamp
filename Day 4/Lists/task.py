states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
                     "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
                     "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
                     "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])


# Negative Indices
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[-1]) #this will be "Pear"

# Modifying Items
# fruits = ["Cherry", "Apple", "Pear"]
# fruits[0] = "Orange"

print(fruits) # fruits will now become ["Orange", "Apple", "Pear"]


 # Adding Items
# You can add items to the end of a List using the append() function. e.g.

fruits.append("Orange")
print(fruits) # fruits will now become ["Cherry", "Apple", "Pear", "Orange"]

states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)

print(fruits.insert(3, "Strawberry"))