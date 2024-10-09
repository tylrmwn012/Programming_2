from arrays import Array

class Deck():
    '''
    This class takes a deck of playing cards and serves the 
    purpose of manipulating the cards in the deck using 
    several different functions.
    
    Member Variables:
        self.__array (array): The initial deck of cards.
        self.__topArray (array): The top half of the deck of cards.
        self.__bottomArray (array): The bottom half
                                    of the deck of cards.
    '''
    '''
    __init__(self, array) [describe function][describe purpose]
    
    Parameters:
        self (referance): Used to access variables from the 
                          initial function.
        array (array): Used to initialize the variables as
                       arrays. 
    
    Returns:
        datatype: none
    '''
    def __init__(self, array):
        self.__array = array
        self.__topArray = array
        self.__bottomArray = array
    
    '''
    __str__(self) takes the deck of cards and returns it
    to the user as a string.
    
    Parameters:
        self (referance): Used to access variables from the 
                          initial function.
    
    Returns:
        string: returns the array of cards as a string, (no
        brackets).
    '''
    def __str__(self):
        return str(self.__array)[1:-1]
    
    '''
    size(self) takes the deck of cards and returns it's length
    as an integer; tells the user the number of cards in the deck. 
    
    Parameters:
        self (referance): Used to access variables from the 
                          initial function.

    Returns:
        integer: returns the size of the array, (number of cards
        in the deck), as an integer
    '''
    def size(self):
        return int(len(self.__array))
    
    '''
    load(self) replaces the current array stored in the deck with
    cards in the second parameter, array. 
    
    Parameters:
        self (reference): Used to access variables from the 
                          initial function.
        array (array): The deck of cards in the initial array.
    
    Returns:
        array: returns the current stored array with the cards
        in the array parameter.
    '''
    def load(self, array):
        for i in range(len(self.__array)):
            self.__array[i] = array[i]
        return self.__array
    
    '''
    cutTop(self) returns the top half of the deck as an
    array, using floor division divided by 2. 
    
    Parameters:
        self (referance): Used to access variables from the 
                          initial function.

    Returns:
        array: returns the top half of the deck of cards as an
        array
    '''
    def cutTop(self):
        self.__topArray = Array(len(self.__array) // 2)
        for i in range(len(self.__topArray)):
            self.__topArray[i] = self.__array[i]
        return self.__topArray
    
    '''
    cutBottom(self) returs the bottom half of the deck of
    cards as an array, using the remainder of the floor division
    divided by 2.
    
    Parameters:
        self (referance): Used to access variables from the 
                          initial function.

    Returns:
        array: returns the bottom half of the array as a
        new array
    '''
    def cutBottom(self):
        self.__bottomArray = Array(-(len(self.__array) // -2))
        for i in range(len(self.__bottomArray)):
            self.__bottomArray[i] = self.__array[i+5]
        return self.__bottomArray
    
    '''
    rotate(self) takes the bottom half of the deck of cards in
    the array and puts it in front of the top half of the deck
    in the array. It takes the bottom half of the array from 
    cutBottom and top from cutTop and uses two while loops to
    add the bottom half of the deck of cards and then the top
    half of the deck of cards to the initial array.
    
    Parameters:
        self (referance): Used to access variables from the 
                          initial function.
        
    Returns:
        array: returns an array with the bottom half in front of 
        the top half of the given deck of cards. 
    '''
    def rotate(self):
        i = 0
        j = 0
        k = 0
        while i < len(self.__bottomArray):
            self.__array[k] = self.__bottomArray[i]
            k += 1
            i += 1
        while j < len(self.__topArray):
            self.__array[k] = self.__topArray[j]
            k += 1
            j += 1
        return self.__array
    
    '''
    reverse(self) changes the deck of cards to reverse order
    of the original array. It uses a temporary array (tempArray)
    to store the cards in reverse order, and then the cards in that
    order are placed back into the original array. 
    
    Parameters:
        self (reference): Used to access variables from the 
                          initial function.
    
    Returns:
        array: returns the array in reverse order of the initial 
        deck of cards.
    '''
    def reverse(self):
        tempArray = Array(len(self.__array))
        for i in range(len(tempArray)):
            tempArray[i] = self.__array[len(self.__array)-i-1]
        for i in range(len(tempArray)):
            self.__array[i] = tempArray[i]
        return self.__array
    
    '''
    shuffle(self) shuffles the deck of cards by performing
    a "perfect out-shuffle."
    
    Parameters:
        self (reference): Used to access variables from the 
                          initial function.

    Returns:
        array: Returns the shuffled deck of cards as an array.
    '''
    def shuffle(self):
        i = 0
        j = 0
        k = 0
        while i < len(self.__topArray):
            self.__array[k] = self.__topArray[i]
            k += 1
            i += 1
            self.__array[k] = self.__bottomArray[j]
            k += 1
            j += 1
        return self.__array

