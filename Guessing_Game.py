import random
Number=random.randint(1,100)
check=False
count=0
while not check:
    x=int(input("Enter the number : "))
    if Number<x:
        print("Guess lower number")
    elif Number>x:
        print("Guess higher number")
    else:
        print("You choose correct number")
        check=True
    count+=1
print(f"You took {count} attempts")
