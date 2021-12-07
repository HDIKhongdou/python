'''
王者荣耀角色管理

角色:姓名,性别,职业

添加角色
删除角色
修改角色
查询角色单个角色
显示所有角色
退出系统

'''

import time

all_role = [] # 存放所有角色'容器'
print('~~~~~~~~~欢迎进入王者荣耀角色管理~~~~~~~~~')
while True:
    choice = input('请选择功能:\n 1.添加角色 \n 2.删除角色 \n 3.修改角色 \n 4.查询角色单个角色 \n 5.显示所有角色 \n 6.退出系统 \n')
    # 判断
    if choice == '1':
        print('添加角色模块:')
        name = input('\t角色名:')
        sex = input('\t性别:')
        job = input('\t职业:')
        role = (name,sex,job)
        # 添加到all_role
        all_role.append(role)
        print('成功添加{}到王者荣耀系统！\n' .format(name))
    elif choice == '2':
        print('删除角色模块：')
        role_name = input('输入角色名：')
        # 查找是否存在此角色名
        for role in all_role:
            if role_name in role:
                # ???? 添加一个是否确定删除询问，确定删除则再删除
                all_role.remove(role)
                print('成功删除角色:{}'.format(role_name))
                break
        else:
            print('本系统不存在角色:{},请检查角色名称。'.format(role_name))
    elif choice == '3':
        print('修改角色模块')
    elif choice == '4':
        print('查询角色模块：')
        role_name = input('\t角色名：')
        # 查找是否存在此角色名
        for role in all_role:
            if role_name in role:
                print('存在此角色信息如下:')
                print('{}{}{}'.format(role[0]).ljust(30),role[1].ljust(30),role[2].ljust(30))
                break
        else:
            print('\t本系统不存在角色:{},请检查角色名称。'.format(role_name))
    elif choice == '5':
        print('显示所有角色模块:')
        print('{}{}{}' .format('名称' .center(10), '名称' .center(10), '职业' .center(10)))
        for role in all_role:
            print(role[0].center(10), end='')
            print(role[1].center(10), end='')
            print(role[2].center(10), end='')
    elif choice == '6':
        print('正在退出王者荣耀管理系统~~~~')
        time.sleep(3)
        print('成功退出')
        break
    else:
        print('输入错误，请重新选择!')