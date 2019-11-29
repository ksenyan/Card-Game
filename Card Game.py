#ok so list of numbers, 2-14 (ace is 14)
#then list of suits
#introduction
#start of round, you are dealt 5 cards and computer is too (or not??)
#cards are in a list, you choose which card to play by writing integer position.
#if the computer has the same suit, it chooses a random card in the suit. if not, all random
#if the suits are the same, the person with the highest value gets 2 points
    ##if not, the person with the highest value gets 1 point.
    ##if the values are the same, nobody gets a point
#next round the computer picks random card
#rounds keep going until someone reaches 10 points.
#celebration at the end

import random, time

suitlist = ['clubs', 'hearts', 'spades', 'diamonds']
numberlist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 

yourpoints = 0
computerpoints = 0

print ("Welcome to the game of suits! You'll be drawn a hand of 5 cards.")
time.sleep(1)
print("You play a card and the computer does too. The one with the highest value takes a point.")
time.sleep(1)
print("If the suits are the same, the one with the highest value gets 2 points!")
time.sleep(1)
print("But if the values are the same, nobody takes a point that round.")
time.sleep(1)
print("You will play until someone reaches 10 points.")
time.sleep(1)
print("The thing is, just like golf, you don't want points. So try and save your low cards!")
time.sleep(1)
print("For simplicity, jack, queen, king, and ace get translated to 11-14")
time.sleep(1)
print("For every point you have, you will owe $1000 at the end of the game.")
time.sleep(1)

yourhand = []                       #start with empty list
for cards in range (5):
    suit = random.choice(suitlist)
    number = random.choice(numberlist)
    card = str(number) + ' of ' + suit #combines a number and suit
    while card in yourhand:            #if the card is already in your hand, it makes a new one
        suit = random.choice(suitlist)
        number = random.choice(numberlist)
        card = str(number) + ' of ' + suit
    yourhand.append(card)

computerhand = []                       #same thing for computer hand
for cards in range (5):
    suit = random.choice(suitlist)
    number = random.choice(numberlist)
    card = str(number) + ' of ' + suit
    while card in yourhand or card in computerhand: #checks both hands           
        suit = random.choice(suitlist)
        number = random.choice(numberlist)
        card = str(number) + ' of ' + suit
    computerhand.append(card)
            
while yourpoints < 10 and computerpoints < 10 :    #play until 10 points  

    print ("This is your hand: ")
    time.sleep(1)
    print (yourhand, sep=', ')

    time.sleep(1)
            
    print ("It's your turn. Pick the index of the card you want to play (1-5). ")

    while True:
        try:
            chosencardnumber = int(input())   #you input
        except ValueError :                 #but if you get an error
            print("Invalid input.")         #it tells you
            continue                        #and makes you retry
        if chosencardnumber <1 or chosencardnumber >5:  #if the error doesn't occur
            print("Invalid number")                     #but the number is outside the index
        elif chosencardnumber <= 5 and chosencardnumber >=1 :
            break
            
    chosencardnumber = int(chosencardnumber)   
    chosencard = yourhand[chosencardnumber-1] #subtract 1 because index starts at 0

    time.sleep(1)
    
    print ("You dealt the card: "+ chosencard)
    yourhand.remove(chosencard)

    spotofspace = int(chosencard.find(' ')) #used to separate value from suit in card
    valuechosencard = chosencard[0:(spotofspace+1)] #everything before first space is value
    yoursuit = chosencard[spotofspace:]             #everything after is suit


    computersuit = [s for s in computerhand if yoursuit in s] #makes list of cards that have the same suit as the one played
    if computersuit != []:                          #if the list is empty
        computercard = random.choice(computersuit)  #it just chooses a random card
    else:
        computercard = random.choice(computerhand)  #otherwise, it chooses a card of that suit

    time.sleep(1)
    print ("The computer dealt: " + computercard)
    
    computerhand.remove(computercard) 
    
    spotofspace = int(computercard.find(' '))
    valuecomputercard = computercard[0:(spotofspace+1)]
    computercardsuit = chosencard[spotofspace:]

    time.sleep(1)

    if yoursuit == computercardsuit:                        #as per game rules
        if int(valuechosencard) > int(valuecomputercard) :
            print("You lost this round and you get 2 points. ")
            yourpoints += 2
        elif int(valuecomputercard) > int(valuechosencard) :
            print ("You won this round and the computer gets 2 points. ")
            computerpoints += 2
    else:
        if int(valuechosencard) > int(valuecomputercard) :
            print("You lost this round and you get 1 point. ")
            yourpoints += 1
        elif int(valuecomputercard) > int(valuechosencard) :
            print ("You won this round and the computer gets 1 point. ")
            computerpoints += 1
        else:
            print("The values are the same and nobody gets a point. ")

    time.sleep(1)
    print ("You have "+ str(yourpoints) + " points.")
    print ("The computer has " + str(computerpoints) + " points.")

    
        
    suit = random.choice(suitlist)              #this section adds a new card to each hand
    number = random.choice(numberlist)          #making sure it's not a repeat
    card = str(number) + ' of ' + suit
    while card in yourhand or card in computerhand: #by checking if it's in a hand already
        suit = random.choice(suitlist)
        number = random.choice(numberlist)
        card = str(number) + ' of ' + suit
    yourhand.append(card)
    while card in yourhand or card in computerhand:
        suit = random.choice(suitlist)
        number = random.choice(numberlist)
        card = str(number) + ' of ' + suit
    computerhand.append(card)

time.sleep(1)
print ("Tthe game is over.")

if yourpoints >= 10:                #calculates points and tells you who won
    print ("Looks like you lost and you owe $10000.")
    print ("However, the computer owes $" + (str(computerpoints*1000))+".")
    print ("Meaning, you only owe $"+ str((10000-int(computerpoints*1000)))+"!")
    print ("Thanks for playing.")
    
elif computerpoints >= 10:
    print ("Looks like you won and the computer owes you $10000.")
    print ("However, you owe $" + (str(yourpoints*1000))+".")
    print ("Meaning, you only get $"+ (str(10000-(int(yourpoints*1000))))+"!")
    print ("Thanks for playing.")
    
