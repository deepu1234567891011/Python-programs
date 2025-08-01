secretnumber=6
guess = int(input("enter a guess number between 1-10:"))
while guess != secretnumber:
    print("your guess is wrong try again")
    guess = int(input("enter a guess number: "))
    print("win")
    
