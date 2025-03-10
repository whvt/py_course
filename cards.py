import random


class Card:
    number_list = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    mast_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
    joker_colors = ["Red", "Black"]

    def __init__(self, mast, number):
        self.mast = mast
        self.number = number

    def __str__(self):
        return f"{self.number} of {self.mast}"


class CardsDeck:
    def __init__(self):
        self.cards = []
        # Add all standard cards
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(mast, number))
        # Add Red and Black Jokers
        for color in Card.joker_colors:
            self.cards.append(Card(color, "Joker"))

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, card_number):
        if 1 <= card_number <= len(self.cards):
            return self.cards[card_number - 1]
        else:
            raise ValueError(f"Card number must be between 1 and {len(self.cards)}")


deck = CardsDeck()
deck.shuffle()

try:
    user_card_number = int(input("Pick your card (1-54): "))
    card = deck.get(user_card_number)
    print(f"Your card is: {card}")
except ValueError as e:
    print(e)
