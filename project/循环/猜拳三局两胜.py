import random

i = 0
player_count = 0
computer_count = 0
while i <= 2:
    player = int(input("1==石头，2==剪刀，3==布"))
    computer = random.randint(1, 3)
    i += 1
    if player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
        print("玩家获胜")
        player_count += 1
    elif player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print("电脑获胜")
        computer_count += 1
    else:
        print("双方平局")
if player_count > computer_count:
    print("玩家获胜")
elif player_count < computer_count:
    print("电脑获胜")
else:
    print("双方平局")
