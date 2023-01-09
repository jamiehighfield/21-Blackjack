import random

original_card_deck, new_card_deck, random_cards, deck_1, deck_2, deck_3, deck_entered, current_round = ['Ace of Hearts', 'Ace of Diamonds', 'Ace of Clubs', 'Ace of Spades', 'Two of Hearts', 'Two of Diamonds', 'Two of Clubs', 'Two of Spades', 'Three of Hearts', 'Three of Diamonds', 'Three of Clubs', 'Three of Spades', 'Four of Hearts', 'Four of Diamonds', 'Four of Clubs', 'Four of Spades', 'Five of Hearts', 'Five of Diamonds', 'Five of Clubs', 'Five of Spades', 'Six of Hearts', 'Six of Diamonds', 'Six of Clubs', 'Six of Spades', 'Seven of Hearts', 'Seven of Diamonds', 'Seven of Clubs', 'Seven of Spades', 'Eight of Hearts', 'Eight of Diamonds', 'Eight of Clubs', 'Eight of Spades', 'Nine of Hearts', 'Nine of Diamonds', 'Nine of Clubs', 'Nine of Spades', 'Ten of Hearts', 'Ten of Diamonds', 'Ten of Clubs', 'Ten of Spades', 'Jack of Hearts', 'Jack of Diamonds', 'Jack of Clubs', 'Jack of Spades', 'Queen of Hearts', 'Queen of Diamonds', 'Queen of Clubs', 'Queen of Spades', 'King of Hearts', 'King of Diamonds', 'King of Clubs', 'King of Spades'], [], [], [], [], [], "", 1
new_card_deck = original_card_deck

def start_game():
    for i in range(0, 21):
        random_card_index = random.choice(range(len(new_card_deck)))
        random_cards.append(new_card_deck[random_card_index])
        new_card_deck.pop(random_card_index)
    deal_random_cards()
    print("Please mentally choose a card from of the 3 piles.\n")
    print_decks()

def deal_random_cards():
    global deck_1, deck_2, deck_3
    deck_1.clear()
    deck_2.clear()
    deck_3.clear()
    for value in random_cards:
        deck_1.append(value) if(len(deck_1) == len(deck_2) and len(deck_1) == len(deck_3)) else deck_2.append(value) if(len(deck_1) != len(deck_2)) else deck_3.append(value)

def next_round():
    merge_cards(prompt_user_for_deck())
    print_decks()

def merge_cards(deck_entered):
    global random_cards, deck_1, deck_2, deck_3
    if(deck_entered == "1"):
        deck_1, deck_2 = deck_2, deck_1
    elif(deck_entered == "2"):
        deck_2 = deck_2
    else:
        deck_3, deck_2 = deck_2, deck_3
    random_cards.clear()
    random_cards.extend(deck_1 + deck_2 + deck_3)
    random_cards.reverse()
    deal_random_cards()

def prompt_user_for_deck():
    deck_entered = ""
    print("\nWhich deck, 1, 2 or 3, is your chosen card in? Type the number of the deck in the box and confirm by pressing [Return].")
    while(not(deck_entered == "1" or deck_entered == "2" or deck_entered == "3")):
        deck_entered = input("Number of deck: ")
    return deck_entered

def print_decks():
    print("Deck 1              Deck 2              Deck 3\n")
    for value in range(0, 7):
        print(deck_1[value] + (" " * (20 - len(deck_1[value]))) + deck_2[value] + (" " * (20 - len(deck_2[value]))) + deck_3[value])

start_game()
for value in range(0, 3):
    next_round()
print("\nYour card was the " + deck_2[3] + ".")
