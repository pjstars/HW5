#Author: Pearl John
#Date: 02/15/2024
#Title:
'''
The code implements a Python program for a treasure hunt game where the players continuously place wagers and attempt to 
grab treasures from a chest containing items such as gold, diamonds, rubies, and more. The game continues until either the 
treasure chest is emptied or the player's bank account runs out of funds.
'''


import random

class TreasureHunt:
    def __init__(self, num_items):
        self.treasure_chest = self.populate_treasure_chest(num_items)
        self.bank_account = 1000

    def populate_treasure_chest(self, num_items):
        #Populate the treasure chest with items.
        items = ['gold', 'diamond', 'ruby', 'silver', 'emerald']
        return random.choices(items, k=num_items)

    def place_wager(self, amount):
        #Place a wager for the treasure grab.
        self.bank_account -= amount
        return amount

    def grab_treasure(self):
        #grab treasures from the chest.
        if self.treasure_chest:
            grabbed_item = random.choice(self.treasure_chest)
            self.treasure_chest.remove(grabbed_item)
            return grabbed_item
        else:
            return None

# Example usage
pirates_game = TreasureHunt(num_items=10)

while pirates_game.bank_account > 0:
    wager = pirates_game.place_wager(100)
    treasure = pirates_game.grab_treasure()
    if treasure:
        print(f"You grabbed a {treasure}!")
        # Increase bank account if treasure grabbed
        pirates_game.bank_account += 600  
    else:
        print("The treasure chest is empty!")
        break

print(f"The game is over! Yourbank account balance is: {pirates_game.bank_account}")
