import random
player=input("Enter Player Name: ")
comp=random.randint(1,50)

you = None

guesses = 0
while comp != you:
    you=int(input("Guess a no. between 1 to 50: "))
    guesses +=1
    if comp == you:
        print(f'{player}, you guessed it right')
        game_over = True
    elif comp<=you:
        print(f'{player}, you guessed wrong. please guess low no.')
    elif comp>=you:
        print(f'{player}, you guessed wrong. please guess high no.')

print(f'{player}, you guessed it in {guesses} guesses')
with open ("highscore.txt",'r') as f:
    highscore = int(f.read())
if guesses<highscore:
    print(f'Previous high score is: {highscore}')
    print(f'{player}, you break the Highscore.')
    with open ('highscore.txt','w') as f:
        f.write(str(guesses))
