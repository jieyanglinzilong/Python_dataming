# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:33:22 2020

@author: Administrator
"""
import sqlite3
import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import sqlite3 as sq

con = sqlite3.connect(r"sales.db")
#con.execute("create table card(name primary key ,phone,QQ,email)")

def main():
    def createtable():
        try:
            con = sq.connect(r"sales.db")
            con.execute("create table card(name,phone,QQ,email)")
            con.commit()
            con.close()
        except:
            pass


    # 新增名片
    def add():
        add = Tk()
        add.geometry('260x140+350+200')
        add.minsize(260, 140)
        add.maxsize(260, 140)
        add.title("新建名片")
        lf = LabelFrame(add, text="请 输 入 ：", labelanchor=N)
        lf.pack()
        Label(lf, text="姓 名：").grid(row=0, column=0)
        Label(lf, text="电 话：").grid(row=1, column=0)
        Label(lf, text="Q Q：").grid(row=2, column=0)
        Label(lf, text="Email：").grid(row=3, column=0)
        name = Entry(lf)
        name.grid(row=0, column=1, columnspan=2)
        phone = Entry(lf)
        phone.grid(row=1, column=1, columnspan=2)
        qq = Entry(lf)
        qq.grid(row=2, column=1, columnspan=2)
        email = Entry(lf)
        email.grid(row=3, column=1, columnspan=2)

        # 确定按钮添加数据
        def qd_event():
            try:
                if name.get() == "":
                    showinfo(title="提示", message="姓名不能为空！")
                    add.destroy()
                else:
                    con = sqlite3.connect(r"sales.db")
                    cardList = (name.get(), phone.get(), qq.get(), email.get())
                    con.execute("insert into card(name,phone,QQ,email) values (?,?,?,?)", cardList)
                    # card = {"姓名":name.get(),"电话":phone.get(),"QQ":qq.get(),"Email":email.get()}
                    # card_list.append(card)
                    con.commit()
                    con.close()
                    add.destroy()
                    show_all()
                    # save_data()
                    showinfo(title="提示", message="新建名片成功！")
            except:
                print("error occur")
                showinfo(title="警告", message="姓名不能重复！")

        # 取消按钮
        def qx_event():
            add.destroy()

        Button(lf, text=" 确  定 ", command=qd_event).grid(row=4, column=2, sticky=W)
        Button(lf, text=" 取  消 ", command=qx_event).grid(row=4, column=1, sticky=E)


    # 显示所有
    def show_all():
        x = dataTreeview.get_children()
        for item in x:
            dataTreeview.delete(item)
        con = sqlite3.connect(r"sales.db")
        cur = con.execute("select * from card")
        for i in cur:
            print(i)
            n = 0
            # dataTreeview.insert('', 1, values=("1","2","3","4"))
            dataTreeview.insert('', n, values=i)
            n += 1


    # 清空数据
    def del_all():
        x = dataTreeview.get_children()
        for item in x:
            dataTreeview.delete(item)


    # 查询名片
    def search_card():
        search = Tk()
        search.geometry('240x50+450+300')
        search.minsize(240, 80)
        search.maxsize(400, 170)
        search.title("查找名片")
        lf = LabelFrame(search, text="请 输 入 ：", labelanchor=N)
        lf.pack()
        Label(lf, text="姓 名：").grid(row=0, column=0)
        name = Entry(lf)
        name.grid(row=0, column=1, columnspan=2)

        # print(name.get())
        def sure():
            con = sqlite3.connect(r"sales.db")
            cur = con.execute("select * from card")
            for i in cur:
                # print(i)
                # print(name.get())
                # print(name.get()==i[0])
                if name.get() == i[0]:
                    print("查找成功")
                    # print(i[0])
                    update(i[0])

                    search.destroy()
                    break
            else:
                showinfo(title="提示", message="没有找到!")

        Button(lf, text="查找", command=sure).grid(row=1, column=1, sticky=N)


    # 修改名片
    def update(n):

        update = Tk()
        update.geometry('400x170+350+200')
        update.minsize(400, 170)
        update.maxsize(400, 170)
        update.title("查找名片")
        lf1 = LabelFrame(update, text="名片信息", labelanchor=N)
        lf1.pack()
        Label(lf1, text="姓 名：").grid(row=0, column=0)
        Label(lf1, text="电 话：").grid(row=1, column=0)
        Label(lf1, text="Q Q：").grid(row=2, column=0)
        Label(lf1, text="Email：").grid(row=3, column=0)
        con = sqlite3.connect(r"sales.db")

        cur = con.execute("select * from card where name ==" + "'" + n + "'")
        print("'" + n + "'")
        for i in cur:
            print(i[0] + i[1] + i[2] + i[3])
            Label(lf1, text=i[0], width=20, anchor=W).grid(row=0, column=1, columnspan=2)
            Label(lf1, text=i[1], width=20, anchor=W).grid(row=1, column=1, columnspan=2)
            Label(lf1, text=i[2], width=20, anchor=W).grid(row=2, column=1, columnspan=2)
            Label(lf1, text=i[3], width=20, anchor=W).grid(row=3, column=1, columnspan=2)
        name = Entry(lf1)
        name.grid(row=0, column=3, columnspan=2)
        phone = Entry(lf1)
        phone.grid(row=1, column=3, columnspan=2)
        qq = Entry(lf1)
        qq.grid(row=2, column=3, columnspan=2)
        email = Entry(lf1)
        email.grid(row=3, column=3, columnspan=2)
        Label(lf1, text="提示！修改名片在空白处输入确认修改即可", anchor=E).grid(row=4, column=0, columnspan=3)

        def xg_event(n):
            print(n)
            print(name.get())
            con = sqlite3.connect(r"sales.db")
            con.execute("update card set name=?,phone=?,qq=?,email=? where name =" + "'" + n + "'",
                        (name.get(), phone.get(), qq.get(), email.get()))
            con.commit()
            con.close()
            update.destroy()
            show_all()

            # 删除名片

        def delete(n):
            con = sqlite3.connect(r"sales.db")
            con.execute("delete from card where name =" + "'" + n + "'")
            con.commit()
            con.close()
            show_all()
            showinfo(title="提示", message="已删除！")
            update.destroy()

        Button(lf1, text="修 改", command=lambda: xg_event(n)).grid(row=5, column=2, sticky=E)
        Button(lf1, text="删 除", command=lambda: delete(n)).grid(row=5, column=1, sticky=E)


    # 退出系统
    def quit():
        root.destroy()


    def about():
        showinfo(title="关于我们", message="面向对象名片管理系统")


    createtable()
    # 创建一个Tk根窗口组件root
    root = Tk()
    root.title("名片管理系统")
    root["width"] = 800
    root["height"] = 500

    # 系统管理菜单栏
    mubar = Menu(root)
    muLogin = Menu(mubar, tearoff=0)
    mubar.add_cascade(label="系统管理", menu=muLogin)
    muLogin.add_command(label="加载数据", command=show_all)
    muLogin.add_command(label="清空数据", command=del_all)
    tc = muLogin.add_command(label="退出", command=quit)

    # 名片管理菜单栏
    muCard = Menu(mubar, tearoff=0)
    mubar.add_cascade(label="名片管理", menu=muCard)
    muCard.add_command(label="显示所有", command=show_all)
    root.bind("<Button-1>,")
    muCard.add_command(label="新建", command=add)
    muCard.add_command(label="查找", command=search_card)
    muCard.add_command(label="保存")

    # 帮助菜单栏
    muHelp = Menu(mubar, tearoff=0)
    mubar.add_cascade(label="帮助", menu=muHelp)
    muHelp.add_command(label="关于", command=about)
    t = Text(root, width=100, height=30)
    t.pack()

    dataTreeview = ttk.Treeview(root, height=19, show='headings', column=('name', 'phone', 'QQ', 'email'))
    dataTreeview.column('name', width=80, anchor="center")
    dataTreeview.column('phone', width=80, anchor="center")
    dataTreeview.column('QQ', width=80, anchor="center")
    dataTreeview.column('email', width=80, anchor="center")

    dataTreeview.heading('name', text='姓名')
    dataTreeview.heading('phone', text='电话')
    dataTreeview.heading('QQ', text='QQ')
    dataTreeview.heading('email', text='邮箱')
    dataTreeview.place(rely=0, relwidth=1)
    Label(root, text='名片管理系统V4.0', bg='white', fg='blue', font=('宋体', 15)).pack(side=BOTTOM, fill='x')
    root["menu"] = mubar
    root.mainloop()
class ui(object):
    def run(self):
        main()

if __name__ == "__main__":
    user = ui()
    user.run()



