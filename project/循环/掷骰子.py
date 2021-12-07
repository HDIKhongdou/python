""""
1.玩游戏要有金币，不然不能玩游戏
2.玩游戏奖励金币1次  充值也可以获取金币
3.10元的倍数  20个金币
4.玩游戏消耗5个金币
5.猜大小：猜对 奖励2个金币 猜错没有奖励      超过6以上就是大，否则为小
6.游戏结束：1.主动退出   2.没有金币退出
7.只要退出则打印金币数，共完了几局
"""""

import random
#金币
coins = 0
#计数器
count = 0
#玩游戏要有金币，不然不能玩游戏
if coins >= 5:
    pass
else:
    #提示充值
    print('金币不足请充值再玩！')
    while True:
        money = int(input('请输入充值金额：'))
        #10元的倍数  20个金币
        if money%10==0 and money>0:
            coins += money//10*20
            print('充值成功！当前金币有%d个'%coins)
            #开启游戏之旅
            print('-----开启游戏-----')
            answer = input('是否开始游戏y/n\n')
            while coins>5 and answer == 'y':
                #扣金币
                coins -= 5
                #赠金币
                coins += 1
                #产生两枚随机的骰子
                m = random.randint(1,6)
                n = random.randint(1,6)
                gusee = input('洗牌完毕，请猜大小：')
                #判断比较
                if gusee == '大' and m+n >= 6 or gusee == '小' and m+n < 6:
                    print('恭喜猜对啦，你赢啦！')
                    coins += 2
                else:
                    print('很遗憾！猜错啦！')
                #玩的次数
                count += 1
                answer = input('是否继续游戏y/n')
                #打印次数和金币数
                print('共玩了%d次，剩余金币%d'%(count,coins))
                break
        else:
            print('不是10的倍数，充值失败！')