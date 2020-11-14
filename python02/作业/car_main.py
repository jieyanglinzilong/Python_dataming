from 作业 import car_tools


class Card(car_tools.Cardss):


    def main(self):
        while True:
            super().show_menu()
            x = input("请输入需要操作的功能:")
            if x in ['0', '1', '2', '3']:
                # 新建名片
                if x == '1':
                    super().new_card()
                # 显示全部
                elif x == '2':
                    super().show_card()
                # 查询名片(之后进行修改或删除操作)
                elif x == '3':
                    super().find_card()
                # 退出名片系统
                elif x == '0':
                    break
            else:
                print("您的输入有误，请重新输入!")
        print()
        print("成功退出名片系统!")


if __name__=="__main__":
    wtt=Card()
    wtt.main()
