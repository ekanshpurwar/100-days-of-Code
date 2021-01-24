import random

def deal_cards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

def calculate_score(cards):

    if sum(cards)==21 and len(cards)==2:
        return 0

    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "You lose. You get over!"

    if user_score==computer_score:
        return "draw"
    elif user_score>21:
        return "You went over. You lose!"
    elif computer_score>21:
        return "Opponent went over. You win!"
    elif computer_score>21:
        return "You win"
    else:
        return "You lose"

def play_game():

    user_cards=[]
    computer_cards=[]
    is_game_over=False

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards {user_cards}, your score {user_score}")
        print(f"Computer first card {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to play another deal and 'n' to pass")
            if user_should_deal=='y':
                user_cards.append(deal_cards())
            else:
                is_game_over=True
    #Once user is done drawing cards its computer turn to draw cards as long as its score is less than 17
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, Your final score {user_score}")
    print(f"Computer final hand {computer_cards}, Computer final score {computer_score}")
    print(compare(user_score,computer_score))

while input("Do ypu want to play the game of Blackjack? Type 'y' for yes or 'n' for no ")=='y':
    play_game()