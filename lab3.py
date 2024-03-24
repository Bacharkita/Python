import random
class Card:
    def __init__(self, suit, value): 
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def getValue(self):
        return int(self._value)


    def getSuit(self): 
        return int(self._suit)

    def __str__(self):
        suits = {
            1: "hearts",
            2: "spades",
            3: "diamonds",
            4: "clubs"
        }
        values = {
            1: "ace",
            2: "two",
            3: "tree",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "jack",
            12: "queen",
            13: "king"
        }
        value = values[self.getValue()]
        suit = suits[self.getSuit()]
        return "{} of {}".format(value, suit)


class CardDeck: 
    def __init__(self):
        self.reset()
    
    def shuffle(self):
        random.shuffle(self._cards)
    
    def getCard(self):
        return self._cards [-1]      

    def size(self):
        return len(self._cards)
    
    def reset(self):
        self._cards = []
        for suit in range(1, 4):
            for value in range(1, 13):
                self._cards.append(Card(suit, value))
                
deck = CardDeck()
deck.shuffle()

while deck.size()>0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()))
    break