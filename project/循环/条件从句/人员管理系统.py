"""
人员管理系统，功能：  添加员工    删除员工    查询员工    修改员工信息

"""
print('------欢迎进入人员管理系统------')
choice = input('请选择功能：\n 1.添加员工:\n 2.删除员工:\n 3.查询员工:\n 4.修改员工信息\n')
if choice == '1':
    print('添加员工')
elif choice == '2':
    print('删除员工')
elif choice == '3':
    print('查询员工')
elif choice =='4':
    print('修改员工信息')
else:
    print('输入错误！')
print('-------------')