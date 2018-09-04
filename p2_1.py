# p2_1.py
"""--- 第一个小游戏 ---"""
temp = input("不妨猜一下我现在心里想的哪个数字: ")
guess = int(temp)

while guess != 8:
    temp = input("哎呀,猜错啦，请重新输入吧: ")
    guess = int(temp)
    if guess > 8:
        print("哥，大了大了~~~")
    if guess < 8:
        print("嘿，小了小了~~~")
    if guess == 8:
        print("你是我肚子里的蛔虫吗?!")
        print("哈哈，猜中了也没有奖励!")

print("游戏结束，不玩啦!")
