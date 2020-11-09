import sys

cardlist = list()
class Card:
    def __init__(self, name, email, phone, age):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
    def find(self, name):
        if (self.name == name):
            print(self.__str__())
    def findObject(self, name):
        if(self.name == name):
            return True
    def updateName(self, newName):
        self.name = newName
    def updateAge(self, newAge):
        self.age =newAge
    def updateEmail(self, newEmail):
        self.email = newEmail
    def updatePhone(self, newPhone):
        self.phone = newPhone
    def __str__(self):
        return ' %s %s %s %s\n'%(self.name, self.age, self.phone, self.email)
def readFile():
    try:
        file = open('data.data', 'r', encoding='utf-8')
        while (1):
            line = file.readline()
            if line:

               CardObjetc = line.split()
               name = CardObjetc[0]
               age  = CardObjetc[1]
               phone = CardObjetc[2]
               email = CardObjetc[3]
               card = Card(name, email, phone, age)
               cardlist.append(card)
            else:
               break

    except Exception:
         file = open('data.data', 'w+')
def findAll():
    print("******本系统的全部用户信息如下")
    print("用户名    邮箱     电话")
    for i in range(len(cardlist)):
        print(cardlist[i])
def findOne():
    for i in range(len(cardlist)):
        card = cardlist[i]
        name = input("输入查找的姓名")
        card.find(name)
def add():
    name = input("输入用户姓名 ")
    email = input("输入用户邮箱 ")
    phone = input("输入用户电话 ")
    age = input("输入年龄")
    card=Card(name, email, phone, age)
    cardlist.append(card)
def delete():
    name = input("输入要删除的用户名")
    for i in range(len(cardlist)):
        card = cardlist[i]
        flag = card.findObject(name)
    if(flag == True):
       cardlist.pop(i)
       print("删除成功")
def update():
    name = input("输入要修改用户的姓名")
    for i in range(len(cardlist)):
       card = cardlist[i]
       flag =card.findObject(name)
       if(flag == True):
           num = input("修改用户名 输入1 修改邮箱输入2 修改电话输入3 修改年龄输入4 ")
           if num == "1":
              newname = input("输入修改的姓名")
              card.updateName(newname)
              break



           if num == "3":

               phone = input("输入电话")
               card.updatePhone(phone)
               break

           if num == "2":
             email = input("输入邮箱")
             card.updateEmail(email)
             break

           if num == "4":
               age = input("输入年龄")
               card.updateAge(age)
               break

       else:
        print("查无此人")
def save():
    file = open('data.data', 'w', encoding='utf-8')
    for card in cardlist:
       print(card.__str__())
       file.writelines(card.__str__())

def main():
    print("*****欢迎使用名片管理系统*****")
    print("输出你想要做的事")
    print("1 添加用户")
    print("2 删除用户")
    print("3 查看所有用户")
    print("4 修改用户信息")
    print("5 保存退出")
    print("6 查找用户请输入")
    num = input("输入您的选择 ")
    readFile()
    if num == "1":
        add()
    if num == "3":
        findAll()
    if num == "2":
        delete()
    if num == "4":
        update()
    if num == "5":
        save()
        sys.exit(0)
    if num=="6":
        findOne()
if __name__=="__main__":
   while(True):
    main()
