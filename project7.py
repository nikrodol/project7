"""
project 7(refactoring project 6)
Program for playing 21 points(russian blackjack) against the computer. Simple model: only numeric values,
poorly developed computer intelligence.
"""

from random import randint


def main():
    print('Hello! Would you like to play the "21 point" (russian blackjack) with computer?', )
    while input().lower() == "yes":
        start()
        print('Are you want play again?')
    else:
        print("It's sad:( Goodbye!")


def start():
    # Инициализируем без генератора колоду так как придется
    # убрать 5ки, да и вообще так экономнее по времени, коду.
    # Колода теперь представляет список всех карт, а не список списков по силе карты
    # так как предидущий вариант не соответсвовал теории вероятности при реальной игре
    coloda = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11]
    your_cards = []
    comp_cards = []
    your_cards = take_card(coloda, your_cards)
    print('Your list of cards:{}'.format(your_cards))
    comp_cards = take_card(coloda, comp_cards)
    game(coloda, your_cards, comp_cards)


def game(coloda, your_cards, comp_cards):
    your_move = randint(0, 1)
    if your_move:
        print('First move is your.')
        your_points = your_move_now(coloda, your_cards)
        print('And second move is copmputer\'s move.')
        comp_points = comp_move_now(coloda, comp_cards)
        who_win(your_points, comp_points)
    else:
        print('First move is computer\'s.')
        comp_points = comp_move_now(coloda, comp_cards)
        print('And second move is your.')
        your_points = your_move_now(coloda, your_cards)
        who_win(your_points, comp_points)
    print(coloda, your_cards, comp_cards)


def your_move_now(coloda, your_cards):
    print('Remember:{}'.format(your_cards))
    print('Are you want take card? If you want you have to say "Yes" ')
    while input().lower() == 'yes' and len(your_cards) < 12:
        your_cards = take_card(coloda, your_cards)
        print('Your list of cards:{}'.format(your_cards))
        print('Maybe some more?')
    else:
        print('Okey')
    return sum(your_cards)


def comp_move_now(coloda, comp_cards):
    while sum(comp_cards) <= 10:
        print('Computer: "Please, croupier give me one card".')
        comp_cards = take_card(coloda, comp_cards)
    while sum(comp_cards) <= 15:
        probability = randint(0, 100)
        if probability > 50:
            print('Computer: "Hem, I think should take one card" ')
            comp_cards = take_card(coloda, comp_cards)
    while sum(comp_cards) <= 18:
        probability = randint(0, 100)
        if probability > 80:
            print('Computer: "I love risk. Give me a card!"')
            comp_cards = take_card(coloda, comp_cards)
    print('Computer: "It is all"')
    return sum(comp_cards)


def take_card(coloda, cards):
    i = randint(0, len(coloda)-1)
    cards.append(coloda[i])
    coloda.pop(i)
    if len(cards) < 2:
        take_card(coloda, cards)
    return cards


def who_win(your_points, comp_points):
    print('Let\'s sum up.')
    print('Your list of cards:{}'.format(your_points))
    print('Computer list of cards:{}'.format(comp_points))
    if your_points < 22 and comp_points < 22:
        if your_points > comp_points:
            print('You are win!')
        elif your_points == comp_points:
            print('It is dead heat, good job guys!')
        else:
            print('You are lose!')
    elif your_points < 22 and comp_points > 21:
        print('You are win!')
    elif your_points > 21 and comp_points < 22:
        print('You are lose!')
    else:
        print('You and computer are lose. It is dead heat')

if __name__ == '__main__':
    main()
