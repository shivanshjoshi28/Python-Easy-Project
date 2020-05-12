import random
li=['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
ch=input('Type "play" to play the game, "exit" to quit:')
while(ch=='play'):
    print()
    attempt=8
    guess_pc=li[random.randint(0,len(li)-1)]
    print(''.join(['-' for i in guess_pc]))
    lii=['-'for i in guess_pc]
    typed=[]
    while(1):
        a=input("Input a letter: ")
        if(len(a)!=1):
            print("You should print a single letter")
        elif not('a'<=a<='z'):
            print("It is not an ASCII lowercase letter")
        elif(a in typed):
            print("You already typed this letter")
        elif (a not in guess_pc):
            print("No such letter in the word")
            typed.append(a)
            attempt-=1


        else:
            typed.append(a)
            for i in range(len(guess_pc)):
                if(guess_pc[i]!=a and lii[i]=='-'):
                    lii[i]='-'
                else:
                    lii[i]=guess_pc[i]
        if(attempt==0):
            print("You are hanged!")
            break
        elif(guess_pc in lii and attempt!=0):
            print()
            print(guess_pc)
            print("You guessed the word!")
            print("You survived!")
            break
        else:
            print()
            print(''.join(lii))
    print()
    ch = input('Type "play" to play the game, "exit" to quit:')
