import random

def hangman():

    answer = ["cat","dog","gollira"]

    a=random.randint(0,2)
    word = answer[a]

#    print(word)


    
    wrong = 0
    stages =["",
             "______________      ",
             "|                   ",
             "|            |      ",
             "|            0      ",
             "|           /|/     ",
             "|           / /     ",
             "|                   "
             ]           


    retters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1 :
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)

        if char in retters:
            cind = retters.index(char)
            board[cind] = char
            retters[cind] = "$"

            #print(retters)
            #print(board)
            

        else:
            wrong += 1

        print("".join(board))

        e = wrong + 1
        
        print("\n".join(stages[0:e]))
#        print(e,len(stages))

        if e == len(stages):
            print("あなたの負け")
            print("正解は{}です".format(word))


        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            

            break

        
            
       #print(board)
            



#    print("\n".join(stages[0:6]))

hangman()
