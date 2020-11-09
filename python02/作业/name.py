import sys
user = []*100
userlist = list()
dellsit = list()
updatelist = list()
n = 0
def main():
      print("*****欢迎使用名片管理系统*****")
      print("输出你想要做的事")
      print("1 添加用户")
      print("2 删除用户")
      print("3 查看所有用户")
      print("4 修改用户信息")
      print("5 退出")
      num= input("输入您的选择 ")
      if num == "1":
          add()
      if num == "3":
          findAll()
      if num == "2":
          delUser()
      if num == "4":
          update()
      if num =="5":
         sys.exit(0)
def add():
    name   =   input("输入用户姓名 ")
    email  = input("输入用户邮箱 ")
    phone  = input("输入用户电话 ")
    user = [name,email,phone]
    userlist.append(user)
    
    print("添加用户{0}成功".format(name))
    
def findAll():
    print("******本系统的全部用户信息如下")
    print("用户名    邮箱     电话")
    for i in range(len(userlist)):
        print(userlist[i])
def delUser():
    name = input("输入要删除的用户名")
    for i in range(len(userlist)):
        dellist = userlist[i]
        
        if dellist[0] == name:
            
            userlist.remove(dellist)
def update():
    print("输入要修改用户的姓名")
    num = input("修改用户名 输入1 修改邮箱输入2 修改电话输入3  ")
    if num == "1":
        name = input("输入姓名  ")
        newname = input("输入修改的姓名")
        
        for i in range(len(userlist)):
           updatelist = userlist[i]
           if updatelist[0] == name:
                  updatelist[0] = newname
                  userlist[i] = updatelist
    if num == "3":
        name = input("输入要修改用户的姓名 ")
        phone = input("输入电话")
        for i in range(len(userlist)):
            updatelist = userlist[i]
            if updatelist[0] == name:
                updatelist[2] = phone
                userlist[i] = updatelist
         
          
    if num == "2":
     name = input("输入要修改用户的姓名 ")
     email = input("输入邮箱")
     for i in range(len(userlist)):
         updatelist = userlist[i]
         if updatelist[0] == name:
            updatelist[1] = email
            userlist[i]=updatelist

    
while True:        
  main()
  print("*****感谢使用再见*****")
