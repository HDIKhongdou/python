'''
产生随机数 random.randint(start,end)
可以猜很多次，直达猜对为止，如果猜错了适当给出提示，猜大了还是猜小了
1.统计猜了几次
2.如果1次就中，赶快去买彩票吧，运气爆了
    2-5，猜对了，运气还可以哦
    6以上，猜对了，运气一般
'''

import random
ran = random.randint(1,50)
count = 0
# 循环才多次
while True:
    guess = int(input('猜一个1-50之间的数字：'))
    # count改变
    count += 1
    #猜对就结束
    if guess == ran:
        if count == 1:
            print('赶快去买彩票吧，运气爆了')
        elif 2<=count<=5:
            print('猜对了，运气还可以哦')
        elif count >= 6:
            print('猜对了，运气一般')
        break
    elif guess > ran:
        print('猜大了，再小一点!')
    else:
        print('猜小了，再大一点!')