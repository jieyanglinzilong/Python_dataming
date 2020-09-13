import getpass
username = input('用户名')
password = getpass.getpass("密码：")
if username == '周悦' and password == '3365' :
    print("登陆成功")
else:
    print("登陆失败")