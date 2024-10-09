from deck import Deck
from helpers import fileToArray
from arrays import Array

def main():
    
    # Change value below to test with different decks.
    testFile = "odddeck.txt"
          
    deck = Deck(fileToArray(testFile)) #reset deck
    print("\n*** TEST LOAD ***")
    print(f"File: {testFile}")
    print(f"Deck size: {deck.size()}")
    print("Deck cards: ", end="")
    print(deck)
    
    deck.load(fileToArray(testFile)) #reset deck
    print("\n*** TEST CUT TOP ***")
    print("Initial deck: ", end="")
    print(deck)
    print(f"Deck size: {deck.size()}")
    print(f"cutTop(): {deck.cutTop()}")
    print(f"cutTop() size: {len(deck.cutTop())}")
    
    deck.load(fileToArray(testFile)) #reset deck
    print("\n*** TEST CUT BOTTOM ***")
    print("Initial deck: ", end="")
    print(deck)
    print(f"Deck size: {deck.size()}")
    print(f"cutBottom(): {deck.cutBottom()}")
    print(f"cutBottom() size: {len(deck.cutBottom())}")   
    
    deck.load(fileToArray(testFile)) #reset deck
    print("\n*** TEST ROTATE ***")
    print("Initial deck: ", end="")
    print(deck)
    deck.rotate()
    print("Rotated deck: ", end="")
    print(deck)
        
    deck.load(fileToArray(testFile)) #reset deck
    print("\n*** TEST REVERSE ***")
    print("Initial deck: ", end="")
    print(deck)    
    deck.reverse()
    print("Reversed cards: ", end="")
    print(deck)
    
    deck.load(fileToArray(testFile)) #reset deck
    print("\n*** TEST SHUFFLE ***")
    print("Initial deck: ", end="")
    print(deck)
    print(f"cutTop(): {deck.cutTop()}")
    print(f"cutBottom(): {deck.cutBottom()}")
    deck.shuffle()
    print("Shuffled cards: ", end="")
    print(deck)    

if __name__ == "__main__":
    main()
