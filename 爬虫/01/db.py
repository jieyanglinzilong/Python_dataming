import sqlite3 as sq
import sys


class Manger:
    def main(self):
        print("*****欢迎使用名片管理系统*****")
        print("输出你想要做的事")
        print("1 添 加 用 户")
        print("2 删 除 用  户")
        print("3 查看所有用户")
        print("4 修改用户信息")
        print("5 查 看 用 户")
        print("6 退     出")
        num = input("输入您的选择 ")
        if num == "1":
            add()
        if num == "3":
            findall()
        if num == "2":
           deleteuser()
        if num == "4":
            update()
        if num == "5":
            findOne()
        if num == "6":
            sys.exit(0)
def findOne():
    id =int(input("输入查询的卡号"))
    con = sq.connect(r"sqles.db")
    cur = con.execute("select*from user where id = ?", (id,))
    for row in cur:
        print(row)

def deleteuser():
    id = int(input("输入要删除的卡号"))
    con = sq.connect(r"sqles.db")
    con.execute("delete from user where id= ?", (id,))
    con.commit()
    con.close()
def createtable():
  con = sq.connect(r"sqles.db")
  con.execute("create table user(id primary key , name , email , phone)")
  con.commit()
  con.close()
def saveone(name,email,phone ):
    con = sq.connect(r"sqles.db")
    i=0
    cur = con.execute("select*from user")
    for row in cur:
        i=row[0]
    id = i+1
    con.execute("insert into user(id,name,email,phone)values(?,?,?,?)", (id, name, email, phone))
    con.commit()
    con.close()
def findall():
    con = sq.connect(r"sqles.db")
    cur = con.execute("select*from user")
    for row in cur:
        print(row)
def updatePhone(id , phone):
    con = sq.connect(r"sqles.db")
    con.execute("update user set phone=? where id=?",(phone,id))
    con.commit()
    con.close()
def updateName(id , name):
    con = sq.connect(r"sqles.db")
    con.execute("update user set name=? where id=?",(name,id))
    con.commit()
    con.close()
def updateEmail(id , email):
    con = sq.connect(r"sqles.db")
    con.execute("update user set email=? where id=?",(email,id))
    con.commit()
    con.close()


def update():
    print("输入要做的事")
    num = input("修改用户名 输入1 修改邮箱输入2 修改电话输入3  ")
    if num == "1":
        id = int(input("输入卡号  "))
        newname = input("输入修改的姓名")
        updateName(id,newname)
    if num == "3":
        id = int(input("输入卡号 "))
        phone = input("输入电话")
        updatePhone(id, phone)


    if num == "2":
        id = int(input("输入卡号 "))
        email = input("输入邮箱")
        updateEmail(id, email)

def add():
     name =input("输入姓名 ")
     email = input("输入邮箱 ")
     phone = input("输入电话  ")
     saveone(name,email,phone)
manger =  Manger()
try :
  createtable()
except Exception:
    pass
while True:
  manger.main()

     
     

