def calculate_love_score(boyfriends_name, girlfriends_name):
    combined_names = boyfriends_name + girlfriends_name
    combined_names = combined_names.lower()

    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")

    true = t + r + u + e

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")

    love = l + o + v + e

    love_score = int(str(true) + str(love))

    print(f"The love score for {boyfriends_name} and {girlfriends_name} is {love_score}")

calculate_love_score("Steven Daniel", "Umu Hawa Barrie")
