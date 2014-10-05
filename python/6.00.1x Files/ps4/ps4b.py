from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    def isValidWord2(word, hand):
    
        handCopy=hand.copy()
        for letter in word:
            if letter in handCopy:
                handCopy[letter]-=1
                if handCopy[letter]<0:
                    return False
            else:
                return False               
                
        return True
        
    maxScore=0

    # Create a new variable to store the best word seen so far (initially None)  
    bestWord=None

    # For each word in the wordList
    for eachWord in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord2(eachWord,hand):
            

            # Find out how much making that word is worth
            wordScore=getWordScore(eachWord, n)

            # If the score for that word is higher than your best score
            if wordScore>maxScore:

                # Update your best score, and best word accordingly
                maxScore=wordScore
                bestWord=eachWord

    # return the best word you found.
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    totalScore=0;
    while True:
        
        if len(hand)>0:
            print "Current Hand: ",
            displayHand(hand)
                        
        word=compChooseWord(hand, wordList, n)
        if word==None:
            break
            

        score=getWordScore(word, n)
        totalScore+=score
        print '"'+word+'" earned ',str(score), " points. Total: ",str(totalScore)+" points"
            
        # Update the hand 
        hand=updateHand(hand,word)

        isHandEmpty=True
        for letter in hand:
            if hand[letter]>0:
                isHandEmpty=False
                break
            
        if isHandEmpty:
            break
        

        
    print "Total score: "+str(totalScore)+" points"
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    newHand={}
    while True:
        choicenr=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choicenr=='r' and len(newHand)==0:
            print "You have not played hand yet. Please play a new hand first!"
        elif choicenr in ('n','r'):
            while True:
                choiceuc=raw_input("Enter u to have yourself play, c to have to computer play: ")
                if choiceuc in ('u','c'):
                    if choicenr=='n':
                        newHand=dealHand(HAND_SIZE) 

                    if choiceuc =='u':
                        playHand(newHand, wordList, HAND_SIZE)
                    else:
                        compPlayHand(newHand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
        elif choicenr=='e':
            break
        else:
            print 'Invalid command.'            

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

def play():
    newHand={}
    while True:
        choicenr=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choicenr=='r' and len(newHand)==0:
            print "You have not played hand yet. Please play a new hand first!"
        elif choicenr in ('n','r'):
            while True:
                choiceuc=raw_input("Enter u to have yourself play, c to have to computer play: ")
                if choiceuc in ('u','c'):
                    if choicenr=='r':
                        if len(newHand)==0:
                            print "You have not played hand yet. Please play a new hand first!"
                        else:
                            if choiceuc=='u':
                                playHand(newHand, wordList, HAND_SIZE)
                            else:
                                compPlayHand(newHand, wordList, HAND_SIZE)
                    else:
                        newHand=dealHand(HAND_SIZE) 
                        if choiceuc=='u':
                            playHand(newHand, wordList, HAND_SIZE)
                        else:
                            compPlayHand(newHand, wordList, HAND_SIZE)

                    break
                else:
                    print 'Invalid command.'
                    

        elif choicenr=='e':
            break
        else:
            print 'Invalid command.'            
