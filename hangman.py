import random
def hangman():
    list=["hangman","laptap","india","pakistan"]
    word=random.choice(list)
    turns=10
    guessmade=''
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word=""
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        if main_word==word:
            print(main_word)
            print("you win")
            break
        print("guess the word",main_word)
        guess=input("enter the guess:")
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid charecter")
            guess=input("enter the guess")
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("-----------")
            if turns==8:
                print("-----------")
                print("     O     ")
            if turns==7:
                print("-----------")
                print("     O     ")
                print("     |     ")
            if turns==6:
                print("-----------")
                print("     O     ")
                print("     |     ")
                print("    /      ")
            if turns==5:
                print("-----------")
                print("     O     ")
                print("     |     ")
                print("    / \     ")
            if turns==4:
                print("-----------")
                print("    \O     ")
                print("     |     ")
                print("    / \     ")
            if turns==3:
                print("-----------")
                print("    \O/    ")
                print("     |     ")
                print("    / \    ")
            if turns==2:
                print("-----------")
                print("    \O/  |  ")
                print("     |     ")
                print("    / \     ")
            if turns==1:
                print("-----------")
                print("    \O/ _ |   ")
                print("     |     ")
                print("    / \     ")
            if turns==0:
                print("you loos the game")
                print("you let a good man die")
                print("-----------")
                print("     O _ |   ")
                print("    /|\     ")
                print("    / \     ")
                break
name=input("enter your name:")
print("wecome",name,"!")
print("---------")
print("try to guess the word less than 10 attemts")


hangman()