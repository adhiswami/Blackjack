import random

cardNum = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cardTypes = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = []
playerValue = 0
compValue = 0
money = 1000
gambleMoney = 0

# Make a deck of cards
for category in cardTypes:
    for card in cardNum:
        deck.append((card, category))

# shuffle & deal cards to player and computer
def deal(deck):
    global compValue, playerValue, compCards, playerCards
    random.shuffle(deck)

    compCards = [deck.pop()]
    compValue = calculatePoints(compCards, compValue)

    playerCards = [deck.pop(), deck.pop()]
    playerValue = calculatePoints(playerCards, playerValue)

    display(compCards, compValue, playerCards, playerValue)

# caculate points each player has
def calculatePoints(userCards, userValue):
    userValue = 0
    for card in userCards:
        if card[0] in ["Jack", "Queen", "King"]:
            userValue += 10
        elif card[0] == "Ace":
            userValue += 11
        else:
            userValue += int(card[0])
    return userValue

def display(compCards, compValue, playerCards, playerValue):
    global money
    print("Computer: ")
    for card in compCards:
        print(*card, end = " / ")
    print("| Computer's Points: ", compValue)
    print()
    print("Player: ")
    for card in playerCards:
        print(*card, end = " / ")
    print("| Player's Points: ", playerValue, " | Money: $", money)

def question():
    playerChoice = input("Do you want to hit or stand? ")
    if playerChoice.lower() == "hit":
        hit()
    elif playerChoice.lower() == "stand":
        stand()
    else:
        question()

# handles gambling question and amount
def gamble():
    global money, gambleMoney
    gambleMoney = int(input("How much would you like to gamble? "))
    if gambleMoney > money:
        print("You entered an amount more than what you have. Try again!")
        gamble()
    else:
        money -= gambleMoney

def updateGamble():
    global money, gambleMoney
    money += 2*gambleMoney
    return money

# when player hits
def hit():
    global compValue, playerValue
    print()
    playerCards.append(deck.pop())
    playerValue = calculatePoints(playerCards, playerValue)
    compCards.append(deck.pop())
    compValue = calculatePoints(compCards, compValue)

# when player stands
def stand():
    global compValue, playerValue, compCards, playerCards
    print()
    compCards.append(deck.pop())
    compValue = calculatePoints(compCards, compValue)

# checks if game is over based on user/comp points
def gameOver(playerValue, compValue):
    if playerValue >= 21:
        return True
    elif compValue >= 21:
        return True

# retry/quit
def tryAgain():
    retry = input("Would you like to keep playing or quit? Type 'r' to retry and 'q' to quit: ")
    if money == 0:
        print("Womp womp, you don't have any money left, so you lose!")
        exit()
    elif retry.lower() == 'r':
        main()
    elif retry.lower() == 'q':
        exit()
    else:
        tryAgain()

def main():
    print("Welcome to Jack Black's Blackjack Nation!")
    deal(deck)
    gamble()
    while not gameOver(playerValue, compValue):
        question()
        display(compCards, compValue, playerCards, playerValue)
    if playerValue > 21:
        print("Womp womp, you lost!")
    elif playerValue == 21:
        print("Whoop-di-woo, you won!")
        updateGamble()  
    elif compValue > 21:
        print("Whoop-di-woo, you won!") 
        updateGamble()  
    elif compValue == 21:
        print("Womp womp, you lost!")

    tryAgain()
    print("Thank you playing with us!")

main()
