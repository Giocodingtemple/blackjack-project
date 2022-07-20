import random

playerIn1 = True
playerIn2 = True
playerIn3 = True
playerIn4 = True
playerIn5 = True
dealerIn = True

# deck of cards / player and dealer hand
deck1 = ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10','hJ','hQ','hK','hA', 
        's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10','sJ','sQ','sK','sA', 
        'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10','cJ','cQ','cK','cA', 
        'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10','dJ','dQ','dK','dA'] 
deck2 = ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10','hJ','hQ','hK','hA', 
        's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10','sJ','sQ','sK','sA', 
        'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10','cJ','cQ','cK','cA', 
        'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10','dJ','dQ','dK','dA']
        
playerHand1 = []
playerHand2 = []
playerHand3 = []
playerHand4 = []
playerHand5 = []
dealerHand = []


# deal the cards
def dealCard(turn):
    card = random.choice(deck1)
    card = random.choice(deck2)
    turn.append(card)
    deck1.remove(card)
    deck2.remove(card)

# calculate total of each hand
def determine_total(hand):
    total = 0
    ace_11s = 0
    for card in hand:
        if card in range(1,14):
            total += card
        elif card in ['h2', 's2', 'c2', 'd2']:
            total += 2
        elif card in ['h3', 's3', 'c3', 'd3']:
            total += 3
        elif card in ['h4', 's4', 'c4', 'd4']:
            total += 4
        elif card in ['h5', 's5', 'c5', 'd5']:
            total += 5
        elif card in ['h6', 's6', 'c6', 'd6']:
            total += 6
        elif card in ['h7', 's7', 'c7', 'd7']:
            total += 7
        elif card in ['h8', 's8', 'c8', 'd8']:
            total += 8
        elif card in ['h9', 's9', 'c9', 'd9']:
            total += 9
        elif card in ['hJ', 'hQ', 'hK', 'sJ', 'sQ', 'sK', 'cJ', 'cQ', 'cK', 'dJ', 'dQ', 'dK', 'h10', 's10', 'c10', 'd10']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total

# check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand1)
    dealCard(playerHand2)
    dealCard(playerHand3)
    dealCard(playerHand4)
    dealCard(playerHand5)

while playerIn1 or dealerIn:
    print(f"The Dealer Kevin Beier had {revealDealerHand()} and X")
    print(f"You have {playerHand1} for a total of {determine_total(playerHand1)}")
    if playerIn1:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if determine_total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn1 = False
    else:
        dealCard(playerHand1)
    if determine_total(playerHand1) >= 21:
        break
    elif determine_total(dealerHand) >= 21:
        break

if determine_total(playerHand1) == 21:
    print(f"\nYou have {playerHand1} for a total of {determine_total(playerHand1)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! You won!!!")
elif determine_total(dealerHand) == 21:
    print(f"\nYou have {playerHand1} for a total of {determine_total(playerHand1)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! House wins!!!")
elif determine_total(playerHand1) > 21:
    print(f"\nYou have {playerHand1} for a total of {determine_total(playerHand1)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("You Busted! House wins!!!")
elif determine_total(dealerHand) > 21:
    print(f"\nYou have {playerHand1} for a total of {determine_total(playerHand1)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House Busted! You win!!!")
elif 21- determine_total(dealerHand) < 21 - determine_total(playerHand1):
    print(f"\nYou have {playerHand1} for a total of {determine_total(playerHand1)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House wins!!!")
elif 21- determine_total(dealerHand) > 21 - determine_total(playerHand1):
    print(f"\nYou have {playerHand1} for a total of {determine_total(playerHand1)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("You win!!!")

while playerIn2 or dealerIn:
    print(f"The Dealer Kevin Beier had {revealDealerHand()} and X")
    print(f"Donald J Trump has {playerHand2} for a total of {determine_total(playerHand2)}")
    if playerIn2:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if determine_total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn2 = False
    else:
        dealCard(playerHand1)
    if determine_total(playerHand2) >= 21:
        break
    elif determine_total(dealerHand) >= 21:
        break

if determine_total(playerHand2) == 21:
    print(f"\nDonald J Trump has {playerHand2} for a total of {determine_total(playerHand2)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! Trump has won!!!")
elif determine_total(dealerHand) == 21:
    print(f"\nDonald J Trump has {playerHand2} for a total of {determine_total(playerHand2)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! House wins!!!")
elif determine_total(playerHand2) > 21:
    print(f"\nDonald J Trump has {playerHand2} for a total of {determine_total(playerHand2)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("You Busted! House wins!!!")
elif determine_total(dealerHand) > 21:
    print(f"\nDonald J Trump has {playerHand2} for a total of {determine_total(playerHand2)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House Busted! Trump has won!!!")
elif 21- determine_total(dealerHand) < 21 - determine_total(playerHand2):
    print(f"\nDonald J Trump has {playerHand2} for a total of {determine_total(playerHand2)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House wins!!!")
elif 21- determine_total(dealerHand) > 21 - determine_total(playerHand2):
    print(f"\nDonald J Trump has {playerHand2} for a total of {determine_total(playerHand2)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Trump has won!!!")

while playerIn3 or dealerIn:
    print(f"The Dealer Kevin Beier had {revealDealerHand()} and X")
    print(f"Kim Jung Un has {playerHand1} for a total of {determine_total(playerHand3)}")
    if playerIn3:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if determine_total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn3 = False
    else:
        dealCard(playerHand1)
    if determine_total(playerHand3) >= 21:
        break
    elif determine_total(dealerHand) >= 21:
        break

if determine_total(playerHand3) == 21:
    print(f"\nKim Jong Un has won {playerHand3} for a total of {determine_total(playerHand3)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! Il has won!!!")
elif determine_total(dealerHand) == 21:
    print(f"\nKim Jong Un has won {playerHand3} for a total of {determine_total(playerHand3)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! House wins!!!")
elif determine_total(playerHand3) > 21:
    print(f"\nKim Jong Un has won {playerHand3} for a total of {determine_total(playerHand3)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("You Busted! House wins!!!")
elif determine_total(dealerHand) > 21:
    print(f"\nKim Jong Un has won {playerHand3} for a total of {determine_total(playerHand3)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House Busted! Il has won!!!")
elif 21- determine_total(dealerHand) < 21 - determine_total(playerHand3):
    print(f"\nKim Jong Un has won {playerHand3} for a total of {determine_total(playerHand3)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House wins!!!")
elif 21- determine_total(dealerHand) > 21 - determine_total(playerHand3):
    print(f"\nKim Jong Un has won {playerHand3} for a total of {determine_total(playerHand3)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Il has won!!!")

while playerIn4 or dealerIn:
    print(f"The Dealer Kevin Beier had {revealDealerHand()} and X")
    print(f"Vladimir Putin has {playerHand4} for a total of {determine_total(playerHand4)}")
    if playerIn4:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if determine_total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn4 = False
    else:
        dealCard(playerHand4)
    if determine_total(playerHand1) >= 21:
        break
    elif determine_total(dealerHand) >= 21:
        break

if determine_total(playerHand4) == 21:
    print(f"\nVladimir Putin has {playerHand4} for a total of {determine_total(playerHand4)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! Putin has won!!!")
elif determine_total(dealerHand) == 21:
    print(f"\nVladimir Putin has {playerHand4} for a total of {determine_total(playerHand4)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! House wins!!!")
elif determine_total(playerHand4) > 21:
    print(f"\nVladimir Putin has {playerHand4} for a total of {determine_total(playerHand4)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("You Busted! House wins!!!")
elif determine_total(dealerHand) > 21:
    print(f"\nVladimir Putin has {playerHand4} for a total of {determine_total(playerHand4)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House Busted! Putin has won!!!")
elif 21- determine_total(dealerHand) < 21 - determine_total(playerHand4):
    print(f"\nVladimir Putin has {playerHand4} for a total of {determine_total(playerHand4)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House wins!!!")
elif 21- determine_total(dealerHand) > 21 - determine_total(playerHand4):
    print(f"\nVladimir Putin has {playerHand4} for a total of {determine_total(playerHand4)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Putin has won!!!")

while playerIn5 or dealerIn:
    print(f"The Dealer Kevin Beier had {revealDealerHand()} and X")
    print(f"Joe Biden has {playerHand5} for a total of {determine_total(playerHand5)}")
    if playerIn5:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if determine_total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn5 = False
    else:
        dealCard(playerHand1)
    if determine_total(playerHand5) >= 21:
        break
    elif determine_total(dealerHand) >= 21:
        break

if determine_total(playerHand5) == 21:
    print(f"\nJoe Biden has {playerHand5} for a total of {determine_total(playerHand5)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! Biden has won!!!")
elif determine_total(dealerHand) == 21:
    print(f"\nJoe Biden has {playerHand5} for a total of {determine_total(playerHand5)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Blackjack! House wins!!!")
elif determine_total(playerHand5) > 21:
    print(f"\nJoe Biden has {playerHand5} for a total of {determine_total(playerHand5)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("You Busted! House wins!!!")
elif determine_total(dealerHand) > 21:
    print(f"\nJoe Biden has {playerHand5} for a total of {determine_total(playerHand5)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House Busted! Biden has won!!!")
elif 21- determine_total(dealerHand) < 21 - determine_total(playerHand5):
    print(f"\nJoe Biden has {playerHand5} for a total of {determine_total(playerHand5)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("House wins!!!")
elif 21- determine_total(dealerHand) > 21 - determine_total(playerHand5):
    print(f"\nJoe Biden has {playerHand5} for a total of {determine_total(playerHand5)} and the dealer Kevin Beier has {dealerHand} for a total of {dealerHand} for a total of {determine_total(dealerHand)} ")
    print("Biden has won!!!")

print(dealerHand)
print(playerHand1)
print(playerHand2)
print(playerHand3)
print(playerHand4)
print(playerHand5)

