

class Cardss(object):

    def __init__(self):
        self.car_list=[]
    #显示功能界面
    @staticmethod
    def show_menu():
        print("*****************************")
        print("             Card            ")
        print()
        print("          1.新建名片           ")
        print("          2.显示全部           ")
        print("          3.查询名片           ")
        print()
        print("          0.退   出           ")
        print("*****************************")


    #新建名片
    def new_card(self):
        name_str=input("请输入姓名:")
        phone_str=input("请输入手机号:")
        qq_str=input("请输入qq:")
        email_str=input("请输入电子邮箱:")

        car_dict={"name":name_str,"phone":phone_str,"qq":qq_str,"email":email_str}

        self.car_list.append(car_dict)
        print("-"*60)
        print(" 姓名\t\t\t","手机号\t\t\t","qq\t\t\t","电子邮箱\t\t\t")
        print("-" * 60)


        for car_dict_1 in self.car_list:
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (car_dict_1["name"],
                                                  car_dict_1["phone"],
                                                  car_dict_1["qq"],
                                                  car_dict_1["email"]))
        print("-" * 60)
        print("新建名片成功！")


    #显示全部名片
    def show_card(self):
        print("-" * 60)
        print(" 姓名\t\t\t", "手机号\t\t\t", "qq\t\t\t", "电子邮箱\t\t\t")
        print("-" * 60)
        if len(self.car_list) > 0:
            for car_dict_1 in self.car_list:
                print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (car_dict_1["name"],
                                                      car_dict_1["phone"],
                                                      car_dict_1["qq"],
                                                      car_dict_1["email"]))
            print()
            print("显示所有名片成功！")
        else:
            print()
            print("表中暂无名片，请选择新建功能添加名片！")


    #查询名片
    def find_card(self):

        find_name=input("请输入需要查询的名字:")



        for car_dict_2 in self.car_list:
            if find_name==car_dict_2["name"]:
                print()
                print("搜索名片成功:")
                print("-" * 60)
                print(" 姓名\t\t\t", "手机号\t\t\t", "qq\t\t\t", "电子邮箱\t\t\t")
                print("-" * 60)
                print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (car_dict_2["name"],
                                                      car_dict_2["phone"],
                                                      car_dict_2["qq"],
                                                      car_dict_2["email"]))
                print("-" * 60)
                cz_str11 = input("请输入需要继续的操作 [1]修改 [2]删除 [0]返回上一级菜单")
                self.deal_card(cz_str11)
                break
        else:
            print()
            print("没有该名片，请重新输入")
            print()

    #对搜索到的数据进行处理（修改/删除）
    def deal_card(self,cz_str):
        for car_dict_2 in self.car_list:

            #修改名片
            if cz_str == '1':

                car_dict_2["name"]= self.new_input(car_dict_2["name"],"请输入修改后的姓名[回车不修改]:")

                car_dict_2["phone"] = self.new_input(car_dict_2["phone"],"请输入修改后的手机号[回车不修改]:")

                car_dict_2["qq"] = self.new_input(car_dict_2["qq"],"请输入修改后的qq[回车不修改]:")

                car_dict_2["email"] = self.new_input(car_dict_2["email"],"请输入修改后的邮箱[回车不修改]:")


                print()
                print("修改完成！")
                print("-" * 60)
                print(" 姓名\t\t\t", "手机号\t\t\t", "qq\t\t\t", "电子邮箱\t\t\t")
                print("-" * 60)
                print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (car_dict_2["name"],
                                                      car_dict_2["phone"],
                                                      car_dict_2["qq"],
                                                      car_dict_2["email"]))
                print("-" * 60)


            # 删除名片
            elif cz_str == '2':
                self.car_list.remove(car_dict_2)
                print()
                print("删除成功!")

    #通过函数来使之按回车返回字典原值。即输入新信息则添加到字典中，如果不输入新信息（按回车）的话就返回原值。

    def new_input(yuanzhi,inputmessage):
        new_input=input(inputmessage)

        if len(new_input)>0:
            return new_input
        else:
            return yuanzhi



