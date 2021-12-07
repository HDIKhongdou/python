"""
键盘上输入以下内容并打印输出:
默认(admin, 1234)
用户名，username
密码，password
是否记住密码bool类型，is_ remember

如果用户名和密码正确并且is_ .remember是True表示记住密码，则打印已经记住用户Xxx的密码啦
否则打印，没有记住密码需要下次继续输入的
"""
username = input('用户名：')
password = input('密码：')
is_remember = False

if username=='admin' and password=='1234':
    # 判断
    if is_remember:
        print('已经记住用户%s的密码啦' % username)
    else:
        print('没有记住密码需要下次继续输入的')
else:
    print('用户名或者密码有错')