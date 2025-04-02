from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = {1: rock, 2: paper, 3: scissors}
game_names = {1: "rock", 2: "paper", 3: "scissors"}

name = input("What is your name? ")
computer_score = 0
user_score = 0

for round_number in range(5):
    print(f"\nRound {round_number + 1}")
    print(f"{name} make your round {round_number + 1} move")

    # Get valid user input
    while True:
        user_choice = int(input(f"{name} what is your choice (type 1 for rock, 2 for paper, and 3 scissors)? "))
        if user_choice in [1, 2, 3]:
            break
        else:
            print(f"Invalid choice! Please enter 1, 2, or 3.")

    computer_choice = randint(1, 3)

    print(f"{name} chose:")
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print(f"It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (
            user_choice == 3 and computer_choice == 2):
        print(f"{game_names[user_choice]} wins!")
        user_score += 1
    else:
        print(f"{game_names[computer_choice]} wins!")
        computer_score += 1

    print(f"{name}'s score: {user_score} vs. computer score: {computer_score}")

    # Check for early win condition
    if user_score >= 2 * computer_score and user_score >= 2:
        if computer_score == 1:
            continue
        print("\nGame ending early!")
        print(f"{name} scores: {user_score} vs. computer scores: {computer_score}")
        print(f"{name} wins 🥇🏆! Your final score is: {user_score}")
        break
    elif computer_score >= 2 * user_score and computer_score >= 2:
        if user_score == 1:
            continue
        print("\nGame ending early!")
        print(f"{name} scores: {user_score} vs. computer scores: {computer_score}")
        print(f"{name}, you lost 😭, Computer wins!")
        break
else:
    # This executes if the loop completes without breaking
    print("\nFinal score after all rounds:")
    print(f"{name} scores: {user_score} vs. computer scores: {computer_score}")
    if user_score > computer_score:
        print(f"{name}, you win!🥇🏆")
    elif computer_score > user_score:
        print(f"{name} you lost 😡, computer wins!")
    else:
        print("It's a tie!⧓")
