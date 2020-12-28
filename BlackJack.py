import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 8
random.shuffle(deck)
rules = """==============================================================================
The rules of BlackJack are simple! Try and achieve a hand value of close but not over 21!
Royal cards [J, Q, K] count as 10 points, while numeric cards carry their face value
An Ace card is special, and can count as 1 or 11 however you like.
If you match or beat the Dealer's hand without going over 21, you win!
If you get over 21 points, you lose, and if the dealer gets over 21 points, you win!
==============================================================================
"""


def deal():
    player_hand = []
    for i in range(2):
        player_card = deck.pop(0)
        if player_card == 11:
            player_card = "J"
        elif player_card == 12:
            player_card = "Q"
        elif player_card == 13:
            player_card = "K"
        elif player_card == 1:
            player_card = "A"
        player_hand.append(player_card)
    return player_hand


def total(card_array):
    total_val = 0
    for card in card_array:
        if card == "J" or card == "Q" or card == "K":
            total_val += 10
        elif card == "A":
            option = int(input("Do you want the Ace to be 1 or 11? Enter the value:\n"))
            if option == 1:
                total_val += 1
            else:
                total_val += 11
        else:
            total_val += int(card)
    return total_val


def hit(card_array):
    new_card = deck.pop()
    if new_card == 11:
        new_card = "J"
    elif new_card == 12:
        new_card = "Q"
    elif new_card == 13:
        new_card = "K"
    elif new_card == 1:
        new_card = "A"
    card_array.append(new_card)
    return card_array


def player(player_cards, player_total):
    option = input("Do you want to hit or stay?").lower()
    if option == "hit":
        player_cards = hit(player_cards)
        print(f"Your new hand is: {player_cards}")
        player_total = total(player_cards)
        print(f"Your current total value is: {player_total}")
        if player_total <= 21:
            player(player_cards, player_total)
        # elif player_total == 21:
        #     print("You got BlackJack! You win!")
        #     play_again()
        else:
            choice = input("You bust! You lose the game!\nWould you like to play again? (Y/N) ").lower()
            if choice == "y":
                game()
            else:
                exit()
    elif option == "stay":
        print(f"Your final total value is: {player_total}")
    return player_total


def dealer_ai(dealer_cards):
    dealer_value = 0
    for card in dealer_cards:
        if card == "J" or card == "Q" or card == "K":
            dealer_value += 10
        elif card == "A":
            if dealer_value <= 10:
                dealer_value += 11
            else:
                dealer_value += 1
        else:
            dealer_value += int(card)

    if dealer_value > 21:
        print("Dealer bust! You win")
        play_again()
    elif dealer_value < 17:
        print(f"The dealer has value of {dealer_value}\nDealer hits")
        dealer_cards = hit(dealer_cards)
        print(f"Dealer new hand is: {dealer_cards}")
        dealer_value = dealer_ai(dealer_cards)
    elif 17 <= dealer_value <= 21:
        print(f"The dealer has value of {dealer_value}\nDealer must stand")

    return dealer_value


def play_again():
    player_choice = input("Would you like to play again? y/n").lower()
    if player_choice == "y":
        game()
    else:
        exit()


def win_condition(player_final_total, dealer_total):
    if dealer_total == player_final_total:
        print("You win by drawing with the dealer!")
        play_again()
    elif dealer_total > player_final_total:
        print("You lose! Dealer has higher hand value!")
        play_again()
    else:
        print("You win! Dealer has lower hand value")
        play_again()


def game():
    print("=============================\nPlayer's turn")
    player_cards = deal()  # holds players first 2 cards
    dealer_cards = deal()  # holds dealers first 2 cards
    print(f"Your hand is: {player_cards}")
    player_total = total(player_cards)  # holds players hand value
    print(f"Your current total is: {player_total}")
    if player_total == 21:
        print("You got BlackJack! You win!")
        play_again()
    print(f"The dealer is showing: {dealer_cards[0]}")
    player_final_total = player(player_cards, player_total)
    print("=============================\nDealer's turn")
    print(f"The dealer has: {dealer_cards}")
    dealer_total = dealer_ai(dealer_cards)
    win_condition(player_final_total, dealer_total)


def introduction():
    print("Welcome to BlackJack!")
    game_start = input("Would you like to [P]lay the game, read the [R]ules, or [Q]uit? ").lower()
    if game_start == "p":
        game()
    elif game_start == "r":
        print(rules)
        introduction()
    elif game_start == "q":
        exit()
    else:
        print("Please enter a valid option")
        introduction()


introduction()