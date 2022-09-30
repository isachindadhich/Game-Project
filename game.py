import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp =='s':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp =='w':
        if you =='g':
            return False
        elif you =='s':
            return True
    elif comp =='g':
        if you =='s':
            return False
        elif you == 'w':
            return True

print("Comp Turn: snack(s), water(w), gun(g)")
randomno = random.randint(1,3)
if randomno==1:
    comp='s'
elif randomno==2:
    comp='w'
elif randomno==3:
    comp='g'

you=input("Your Turn: snack(s), water(w), gun(g): ")
a=gamewin(comp,you)

print(f'comp choose: {comp}')
print(f'you choose: {you}')

if a == None:
    print("Game Tie")
elif a == True:
    print("You Win")
elif a == False:
    print("You Lose")
