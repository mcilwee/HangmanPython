'''
J MCILWEE 10/11/2020
text based hangman game
should be supplied with wordlist called 'Words.txt'
words should be on individual lines with spaces as ' '
'''


import random

def Play():
    blank_hangman=' =------, \n |        \n |         \n |         \n/ \ '
    places=[[19,'o'],[30,'|'],[29,'/'],[31,'\\'],[41,'/'],[43,'\\']]
    Words=[]
    file = open('Words.txt','rt')
    for word in file:
        Words.append(word.rstrip())
    used=[]
    word=random.choice(Words)
    lives=0
    gh=blank_hangman

    game_str=''
    for i in word:
        if i == ' ':
            game_str+='    '
        else:
            game_str+='_ '

    ref_str=' '.join(word)

    while True:
        print('\n'+gh)
        print(game_str)

        print('used letters;',*used)

        guess=input('guess letter - ')
        if guess=='q':
            break
        while not guess.isaplha() or len(guess)>1:
            guess=input('not valid guess\nguess again - ') 

        for i in used:
            if i == guess:
                guess=input('already used.\nguess other letter - ')

        check=False
        for letter in range(len(ref_str)):
            if ref_str[int(letter)] == guess:
                game_str=game_str[0:letter]+guess+' '+game_str[letter+2:]
                check=True
        
        if check==False:
            ref=places[lives][0]
            gh=gh[0:ref]+places[lives][1]+gh[ref+1:]
            lives+=1
        
        used.append(guess)

        if lives>5:
            print(gh)
            print('\nyou lose\n')
            print('the word was',word)
            break
        
        check=True
        for i in game_str:
            if i == '_':
                check=False
        if check==True:
            print('\nyou win\n')
            break
            
Play()
        




