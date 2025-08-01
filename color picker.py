import random
color_names=['red','green','blue','yellow','pink','orange']
color=random.choice(color_names).lower()#computer selecting colour names randomly
#print available colors
print("available colors are:",color_names)
# taking loop for user choice 4 times it will ask
for attempt in range(4):
    user=input("enter a your guess of color:").strip().lower()#user enter the color randomly
    #if user enter color and computer color are mathed it will print winner other wise else stament
    if user==color:
        print("hey your winner keep going deepu!!")
        break
    else:
        print("wron please try again....")
else:
    print("computer choice is",color)

    


