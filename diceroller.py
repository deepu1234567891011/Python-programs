import random
attempt=5
while(attempt>0):
    user=input("Do you want  to roll the dice (yes/no)")
    if user=='yes':
        computer=random.randint(1,100)
                 
        print("the dice rolled",computer)
    elif user=='no':
        print("good bye,thanks for playing")
        break
    else:
        print(" please enter 'yes' or 'no' ")