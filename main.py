"""
-- Python Bootcamp Milestone Project 2 -- 

Author: Botan Bulut
Date: 10/8/2022
"""

# Imports

from random import shuffle

# Global Variables

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
CHOICES = ["H", "h", "s", "S", "A", "a", "P", "p", "D", "d","C", "c"]
YES_NO = ["Y", "y", "N", "n"]

# Classes

class Card():
    
    """Card class that defines its suit and rank"""
    
    
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        
    
    def __str__(self):
        
        return self.rank + " of " + self.suit



    
class Deck():
    
    """Deck class will have 52 cards in it"""
    
    def __init__(self):
        
        self.deck = []
        
        for x in SUITS:
            
            for y in RANKS:
                
                self.deck.append(Card(suit = x, rank = y))
                
    
    def __str__(self):
        
        str_deck = ""
        
        
        for i in self.deck:
            
           str_deck = str_deck + i.__str__() + "\n" 
            
            
        return str_deck 
    
    
    def deal(self):
        
        dealed = self.deck.pop()
        
        return dealed
    
    def shuffle(self):
        
        shuffle(self.deck)
        



class Hand():
    
   
    """Hand class tells the players about the contents of their hand"""
    
    
    def __init__(self):
        
        self.hand = []
        self.aces = 0
        self.value = 0
             
                      
    def hit(self, deck):
        
        self.hand.append(deck.deal())
        
        if self.hand[-1].rank == "Ace":
                
                self.aces += 1
                
        self.value += VALUES[self.hand[-1].rank]
        
        
    def __str__(self):
        
        str_hand = ""    
        
        for _ in self.hand:
            
            str_hand = str_hand + _.__str__() + "\n"
        
        return "------------------------------------------\n" + str_hand + f"Hand value is : {self.value}\nUnadjusted ace count: {self.aces}\n------------------------------------------"
    
    
    def adjust_ace(self):
        
        if self.aces >= 1 and self.value > 21:
            
            self.value = self.value - 10
            self.aces -= 1
            print("1 ace value is adjusted to 1")
        
        else:
            
            print("Adjustment is not possible")


class Chips():
    
    """Chips class tracks player's chips"""
    
    def __init__(self):
        
        self.chips = 100
        
        
    def add(self, value):
        
        self.chips = self.chips + value
        
    
    def subtract(self, value):
        
        self.chips = self.chips - value
        
    
    def __str__(self):
        
        return f"Player has {self.chips} chips"
    

# Functions

def win_check(player, dealer):
    
    if player > 21:
        
        print("Player Busts")
        
        return False
    
    elif player == 21:
        
        print("Player Blackjack!")
        
        return True
    
    elif player < 21 and player >= dealer:
        
        print("Player Wins!")
        
        return True
    
    elif player < 21 and dealer > 21:
        
        print("Dealer Busts!")
        
        return True
    
    else:
        
        print("Dealer Wins!")
        
        return False


def bet_result(account, bool, bet):
    
    if bool == True:
        
        print("Player won the bet")        
        account.add(bet)
        print(account)
        
    else:
        
        print("Player lost the bet\nNo chips is gained")
        account.subtract(bet)
        print(account)


# Main 

game_on = True
round_on = True
dummy1 = True
account = Chips()

while game_on == True:
    
    print("Welcome to the blackjack game! You will be playing against a bot dealer. Good luck!")
    

    
    
    while round_on == True:
        
        new_deck = Deck()
        new_deck.shuffle()
        
        player = Hand()
        
        
        player.hit(deck = new_deck)
        player.hit(deck = new_deck)
        
        dealer = Hand()
        dealer.hit(deck = new_deck)
        dealer.hit(deck = new_deck)
             
        print(account)    
        user_bet_input = input(f"Select bet ammount (maximum bet input is {account.chips}) : ")
        
        while user_bet_input.isdigit() == False or int(user_bet_input) < 0 or int(user_bet_input) > account.chips:
            
            user_bet_input = input("Please enter a valid input: ")
        
        user_bet_input = int(user_bet_input)
            
        while dummy1 == True:
            
            user_choice = input("------------------------------------------\nWhat do you want to do?\n(H)it\nSee (P)layer hand\nSee player (C)hips\nSee (D)ealer's card\n(S)tay and end turn\n(A)djust for Ace (if possible)\n===> ")
            
            while user_choice not in CHOICES:
                
                user_choice = input("Please enter a valid input (H/P/D/S/A): ")
            
            if user_choice == "H" or user_choice == "h":
                
                player.hit(deck = new_deck)
                
                print("Added new card to player hand!")
                print(player)
            
            
            if user_choice == "P" or user_choice == "p":
                
                print(player)
                
                
            if user_choice == "D" or user_choice == "d":
                
                print(f"{dealer.hand[-1].__str__()} with value of {VALUES[dealer.hand[-1].rank]}")
                
            
            if user_choice == "S" or user_choice == "s":
                
                print("Player stays with the hand:")
                print(player)
                
                dummy1 = False
                
            
            if user_choice == "A" or user_choice == "a":
                
                player.adjust_ace()
                print(player)

            if user_choice == "C" or user_choice == "c":
                
                print(account)

        
        while dealer.value <= 16 and dealer.value < player.value:
            
            print("Dealer hits")
            dealer.hit(deck = new_deck)
        
        
        if dealer.value > 21 and dealer.aces >= 1:
            
            print("Dealer Adjusts his one ace")
            dealer.adjust_ace()
        
        
        print("Dealer has:")
        print(dealer)
        
        win = win_check(player = player.value, dealer = dealer.value)
        
        bet_result(account = account, bool = win, bet = user_bet_input)
        
        user_game_decsion = input("Round is over do you wish to play again? (Y/N)")
        
        while user_game_decsion not in YES_NO:
            
            user_game_decsion = input("Wrong input: ")
        
        if user_game_decsion == "N" or user_game_decsion == "n":
            
            if account.chips == 0:
                
                print("Player has 0 chips. Game Over!")
                quit()
                
            else:
                
                print(account)
                print(f"Player ends the game with {account.chips} chips")
                print("Thanks for playing. Remember House always wins ;)")
                game_on = False
                quit()
        
        else:
            
            if account.chips == 0:

                    print("Player has 0 chips. Game Over!")
                    quit()
            else:
                        
                round_on = True
                dummy1 = True
        
          
   