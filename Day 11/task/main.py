from random import choice
from art import *

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(users_score, computers_score):
    if users_score == computers_score:
        return "Draw 😡"
    elif computers_score == 0:
        return "You lose, Opponent has a Blackjack 😱"
    elif users_score == 0:
        return "You win with a Blackjack 😎"
    elif users_score > 21:
        return "You went over. You lose 😭"
    elif computers_score > 21:
        return "Opponent went over. You win 😁!"
    elif users_score > computers_score:
        return "You win 🥇"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False


    for _ in range(2):
        new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(F"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or type 'n' to pass: ")
            if user_should_deal != 'y':
                is_game_over = True
            else:
                user_cards.append(deal_card())

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

print("\n" * 20)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()
