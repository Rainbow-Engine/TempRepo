import random

def janken():
    choices = ["グー", "チョキ", "パー"]
    computer_choice = random.choice(choices)
    
    print("じゃんけんを始めます！")
    print("1: グー")
    print("2: チョキ")
    print("3: パー")
    
    player_choice = int(input("選択肢の番号を入力してください: "))
    player_choice -= 1
    
    if player_choice < 0 or player_choice >= len(choices):
        print("正しい選択肢を入力してください。")
        return
    
    print("あなたの選択: ", choices[player_choice])
    print("コンピュータの選択: ", computer_choice)
    
    if player_choice == (choices.index(computer_choice) + 1) % len(choices):
        print("あなたの勝ちです！")
    elif player_choice == (choices.index(computer_choice) - 1) % len(choices):
        print("あなたの負けです！")
    else:
        print("引き分けです！")

# じゃんけんを実行
janken()