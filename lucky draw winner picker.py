import random
lucky_draw=["deepu","swapna","deepika","narayana","mounika","pujitha"]
print("show the names of lucky draw",lucky_draw)
computer = random.choice(lucky_draw).lower()
for attempt in range(5):
    user=input("enter your random name ").strip().lower()
    if user==computer:
        print("congratulations your the winner of the game",computer)
        break
    else:
        print("please try again once")
else:
    print("the choice of the random name of the  computer is:",computer)
    

    




