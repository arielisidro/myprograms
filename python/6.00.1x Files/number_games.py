print ("Please think of a number between 0 and 100! ")
        
l=0
h=100
ans=''

while ans!='c':
    guess=(l+h)/2
    print("Is your secret number " + str(guess))
    ans=raw_input("Enter h to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low.\
Enter 'c' to indicate I guessed correctly. ")
    if ans=='l':
        l=guess
    elif ans=='h':
        h=guess
    elif ans=='c':
        print("Game over. Your secret number was: "+str(guess))
    else:
        print ("Sorry, I did not understand your input.")
           