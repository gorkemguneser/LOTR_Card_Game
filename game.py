##########################################   FUNCTIONS LIST ################################################

def first_seven_cards(playerhands,seven_cards):
    for i in seven_cards:
        playerhands[i] = cards_dict[i]
        
############################################################################################################
        
def remove_cards_from_players(cardsinhands,playersdeck):
    for keys in cardsinhands.keys():
        for j in playersdeck:
            if keys == j:
                playersdeck.remove(keys)

############################################################################################################
                
def player_turn(hand,deck,field):
    #print(player_1_deck)
    #print(hand)
    if len(hand) < 7 and len(deck) != 0:
        hand[deck[0]] = cards_dict[deck[0]]
        del deck[0]
    
    print(hand)
    print('What is your move? Please specify card name.')

    x = input()
    if str(x) in hand.keys():
        print('Your move is', x ,'with attack power',hand[x])
        field.append(hand[x])
        #print(hand[x])
        del hand[x]
        return (x,field[-1])

    else:
        return player_turn(hand,deck,field)
    print('Player one has', x , ':' , cards_dict[x] , 'on the field')
    
############################################################################################################

def comparecardpowers(field1,field2,player1health,player2health):
    
    #global player_1_total_health
    #global player_2_total_health
    #field2 = [100]

    print('\n\nThe clash between Player 1 and Player 2 has started.')
    if field1[-1] > field2[-1]:
        player2health = player_2_total_health - (field1[-1] - field2[-1])
        #print(player2health)
        print('\n\nPlayer 1 has WON this clash!', field1[-1] - field2[-1] ,"health points will be deducted from Player 2's total health.")
    elif field1[-1] < field2[-1]:
        player1health = player_1_total_health - (field2[-1] - field1[-1])
        print('\n\nPlayer 2 has WON this clash!', field2[-1] - field1[-1] ,"health points will be deducted from Player 1's total health.")
    elif field1[-1] == field2[-1]:
        print('\n\nRound is DRAW.')
    return (player1health, player2health)

############################################################################################################

def winnercheck_end_game(health1,health2):
    if health2>health1:
        
        print('----------------------------- CONGRATULATIONS! Player 2 HAS WON THE GAME. -----------------------------')
        print('\n')
        print('oOo ' * 30)
        
    elif health1>health2:
        print('----------------------------- CONGRATULATIONS! Player 1 HAS WON THE GAME. -----------------------------')
        print('\n')
        print('oOo ' * 30)  
        
    elif health1==health2:
        print('----------------------------- GAME OVER! THERE IS NO WINNER. -----------------------------')
        print('\n')
        print('oOo ' * 30)



import random


print("WELCOME TO THE LORD OF THE RINGS CARD GAME! \n\n\n RULES: \n\n 1) Players start to game with 7 cards and players also have 18 cards in their decks.\n 2) In each round, players place a card onto the field. In the end of every turn, cards will be removed from the field. Player will pull one new card from the deck automatically. \n 3) Once both players placed a card to the field, the difference between card powers will be deducted from defeated player's total health. \n 4) Player with higher health points wins after 10 rounds. \n 5) If player's total health decreases to 0 before end game, player lost.\n ")

rounds  = 0

player_1_total_health = 1200
player_2_total_health = 1200

player_1_deck = []
player_1_hand = []

player_2_deck = []
player_2_hand = []

player_1_field=[]
player_2_field=[]


cards_dict = {'Morgoth':2500,'Sauron':2150,'Witch King':1980,'Gimli':2020,'Isildur':1890,'Elendil':1760,'Khamul':1880,'Saruman':1980,'Gollum':1675,'Balrog':1960,'Gothmog':1780,'Green Goblin':1780,'Smaug':1930,'Freddy':1750,'Legolas':2100,'Gandalf':2170,'Faramir':1770,'Aragorn':2120,'Frodo':1750,'Bilbo Baggins':1780,'Galadriel':2320,'King of Dead':1990,'Nazgul':1890,'Arwen':1880,'Elrond':1790,'Peregrin':1680,'Sam':1400,'Gorkem':2300,'Elf':1500,'Human':1600,'Dwarf':1300,'Orc':1400,'Wolf':1700,'Azog':1900,'Bolg':1760,'Gorbag':1600,'Golfimbul':1400,'Shadowfax':1680,'Warg':1630,'Durin':1460,'Urukhai':1650,'Ogre':1750,'Troll':1830,'Ent':1990,'Shelob':1820,'Great Eagle':1700,'Giant':1850,'Ungoliant':2050,'Glaurung':2210,'Ghost':1700}


player_1_deck = random.sample(list(cards_dict), 25)
player_2_deck = random.sample(list(cards_dict), 25)


player_1_first_7_cards=random.sample((player_1_deck),7)
player_2_first_7_cards=random.sample((player_2_deck),7)    


hand1={}
hand2={}


first_seven_cards(hand1,player_1_first_7_cards)
first_seven_cards(hand2,player_2_first_7_cards)



while rounds < 7 and player_1_total_health > 0 and player_2_total_health > 0:
    
    
    remove_cards_from_players(hand1,player_1_deck)
    remove_cards_from_players(hand2,player_2_deck)
    
    
    print('\n' *2)
    print('oOo ' * 30)
    print('\n')
    print(' '*40,'ROUND NUMBER: ', rounds+1)
    print('\n')
    print('PLAYER 1 TOTAL HEALTH: ', player_1_total_health)
    print('PLAYER 2 TOTAL HEALTH: ' ,player_2_total_health)
    print('\n' *2)
    
    
    player_turn(hand1,player_1_deck,player_1_field)
    player_turn(hand2,player_2_deck,player_2_field)
    
    
    compareResultTuple = comparecardpowers(player_1_field,player_2_field,player_1_total_health,player_2_total_health)
    player_1_total_health = compareResultTuple[0]
    player_2_total_health = compareResultTuple[1]
    
    
    print('\n' *3)
    

    rounds += 1

    
winnercheck_end_game(player_1_total_health,player_2_total_health)
