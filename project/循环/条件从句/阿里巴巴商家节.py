'''
阿里巴巴商家书，用户名，消费总金额， 账户金额，优惠券
输入购买总购买金额，
如果金0-500则是Lv1级别，
如果500-2000元则是lv2, 2000以上是Lv3

lv1:随机赠送3张1 -10的优惠券，
lv2:赠送2张50元优惠券，如果充值则送充值金额的10%
lV3:赠选2张100优惠券，如果充值则送15%的金额
'''
import random

username = '孙健'
total = int(input('请输入消费金额：'))# 消费金额
money = 0 # 账户金额
coupon = 0 # 优惠券

# 根据总金额判断级别
if 0<total<500: # lv1
    # 随机赠送3张1-10的优惠券
    quan1 = random .randint(1,10)
    quan2 = random .randint(1,10)
    quan3 = random .randint(1,10)
    # 将券数相加
    coupon = quan1+quan2+quan3
elif 500 <= total <2000: # lv2
    # 赠送2张50元优惠券，如果充值则送充值金额的10%
    #嵌套if
    coupon = 100
    recharge=input('%s，是否要充值（送充值金额的10%)?(y/n)')
    if recharge == 'y':
        money += 1.1*int(input('输入充值金额:'))
elif total >= 2000: # lV3
    coupon = 200
    #赠选2张100优惠券，如果充值则送15%的金额
    recharge=input('%s,是否要充值（送充值金额的15%)?(y/n)')
    if recharge =='y':
        money += 1.5*int(input('输入充值金额:'))
print(coupon , money)