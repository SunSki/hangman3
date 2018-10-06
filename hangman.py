def hangman(word):

    letters = list(word) #wordをリスト化する、何番目の文字が正解したか見るため
    board = ["_"] * len(word) #
    wrong = 0
    stages = [" _________     ",
                      "|                          ",
                      "|                   |      ",
                      "|                  O     ",
                      "|                / | \   ",
                      "|                 / \    "
             ]
    win = False #勝ち負けフラグ
    
    #最初の画面表示
    print("welcome to HANGMAN!")

    #終わるまでループ
    while(wrong < len(stages) - 1):
        print("\n")
        char = input("Predict a letter:")
        i = 0
        #正解した時
        if char in letters:
            for l in letters:
                if char == l:
                    board[i] = char
                i+=1
        #間違えた時
        elif len(char) == 1:
            wrong += 1
            print("it's a pity...")
        #不正確な入力
        else:
            print("input a proper letter")
        
        print(" ".join(board))
        print("\n".join(stages[0: wrong+1]))
        
        #勝った時
        if "_" not in board:
            print("You win! Word:{}.".format(word))
            print("\n".join(stages[0: wrong+1]))
            win = True
            break
    
    #負けた時
    if not win:
        print("You lose... Word:{}.".format(word))
        print("\n".join(stages[0: wrong+1]))