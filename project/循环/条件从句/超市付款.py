'''
模拟超市付款: 商晶单价 商品数量
    键盘上输入商品单价，以及商品数量，
        然后计算应付总额
        计算总额  float
    提示用户可以有4种付款方式
        不同的付款方式有不同的折扣:先展示四种付款方式
         现金没有折扣
         微信0.95折
         支付宝鼓励金付款金额的10%    鼓励金可以直接折算到付款金额中
         刷卡满100-20
'''
print('欢迎光临北科超市')
price = float(input('商品单价：'))
number = int(input('商品数量：'))
# 计算总额
total = price*number
# 选择付款方式
choice = input('选择付款方式：1.现金，2.微信，3.支付宝，4.刷卡 ')
# 判断
if choice == '1':
    print('现金没有折扣,应付金额是：%.2f' % total)
elif choice == '2':
    print('微信0.95折')
    total *= 0.95
    print('支付金额是::%.2f' % total)
elif choice == '3':
    print('支付宝鼓励金付款金额的10%，鼓励金可以直接折算到付款金额中')
    total = total - total*0.1
    print('支付金额是::%.2f' % total)
elif choice == '4':
    print('刷卡满100-20')
    if total > 100:
        total -= 20
        print('支付金额是::%.2f' % total)
    else:
        print('没有折扣，支付金额是::%.2f' % total)
else:
    print('输入错误！~')