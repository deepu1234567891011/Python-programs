n=int(input("enter a numbers"))
while(n<=30):
    print(n)
    n+=1
    if(n%2==0):
        print("aaza")
    if(n%3==0):
        print("baza")
    if(n%5==0):
        print("caza")
    if(n%2==0 and n%3==0):
        print("aazabaza")
    if(n%3==0 and n%5==0):
        print("bazacaza")
    if(n%2==0 and n%5==0):
        print("aazacaza")
    if(n%2==0 and n%3==0 and n%5==0):
        print("aazabazacaza")
    
    
