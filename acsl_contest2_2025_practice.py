class Card:
    def __init__(self, card_data):
        self.color = ""
        self.shape = ""
        self.number = ""
        self.is_wild = False
        colors = set(["R", "G", "B", "Y"])
        shapes = set(["O", "T", "X", "S"])
        if(len(card_data) == 3):
            self.color = card_data[0]
            self.number = card_data[1]
            self.shape = card_data[2]
            self.is_wild = False
        else:
            if(card_data[0] in colors):
                self.color = card_data[0]
            elif(card_data[0] in shapes):
                self.shape = card_data[0]
            else:
                self.number = card_data[0]
            self.is_wild = True
        
def is_playable(card, pile_card):
    if(card.is_wild == False):
        count = 0
        if(card.color == pile_card.color):
            count += 1
        if(card.number == pile_card.number):
            count += 1
        if(card.shape == pile_card.shape):
            count += 1
        return count == 2
    else:
        return card.color == pile_card.color or card.number == pile_card.number or card.shape == pile_card.shape

def play_hand(hand, pile_card1_data, pile_card2_data):
    i = 0
    while (i < len(hand)):
        card = Card(hand[i])
        pile_card1 = Card(pile_card1_data)
        pile_card2 = Card(pile_card2_data)
        if(is_playable(card, pile_card1) or is_playable(pile_card1, card)):
            pile_card1_data = hand[i]
            hand.remove(hand[i])
            i = 0
        elif(is_playable(card, pile_card2) or is_playable(pile_card2, card)):
            pile_card2_data = hand[i]
            hand.remove(hand[i])
            i = 0
        else:
            i += 1
        
    return pile_card1_data, pile_card2_data, hand

pile = input().split()
hand = input().split()
second_hand = input().split()
pile_card1, pile_card2, remaining = play_hand(hand, pile[0], pile[1])
new_hand = remaining + second_hand
final_pile_card1, final_pile_card2, final_remaining = play_hand(new_hand, pile_card1, pile_card2)

print(len(final_remaining), final_pile_card1, final_pile_card2)