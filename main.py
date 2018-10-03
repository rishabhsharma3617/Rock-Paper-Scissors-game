import random as r

#This function will convert the random integer value to r, p, s.
def convertor(input1):
    test = 'rps'
    return test[input1]

#This function will evaluate the winner based on the conditions.
def printWinner(a,b):
    if (player==comp):
        print("DRAW")
    #For Rock Case
    elif(player=='r' and comp=='p'):
        print("Computer Wins")
    elif(player=='r' and comp=='s'):
        print("Player Wins")
    #For Paper Case
    elif(player=='p' and comp=='r'):
        print("Player Wins")
    elif(player=='p' and comp=='s'):
        print("Computer Wins")
    #For Scissors Case
    elif(player=='s' and comp=='r'):
        print("Computer Wins")
    elif(player=='s' and comp=='p'):
        print("Player Wins")
    return

#This function will show some graphical content on screen during run time
def toAsciiChar(a):
    if(a=='p'):
        return "|"
    if(a=='r'):
        return "O"
    if(a=='s'):
        return "8<"

player = input("Rock(r) , Paper (p) or Scissors (s) ")
player.lower()
comp = r.randint(0,2)  #comp means computer
comp = convertor(comp)
print(toAsciiChar(player)," VS ",toAsciiChar(comp))
printWinner(player,comp)
