capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List inside a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print Lille
print(travel_log["France"][1])


# Nesting Lists inside other Lists

# print letter D
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nesting a Dictionary inside a Dictionary

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# Figure out how to print out "Stuttgart" from the following list:
print(travel_log["Germany"]["cities_visited"][-1])

# Loop through the travel log and print visit information
for country, details in travel_log.items():
    for city in details["cities_visited"]:
        print(f"I have visited {city} {details['total_visits']} times when I went to {country}.")

print()


for country, details in travel_log.items():
    cities = ", ".join(details["cities_visited"])  # Join cities into a single string
    print(f"I have visited {cities} a total of {details['total_visits']} times when I went to {country}.")