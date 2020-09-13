import datetime
sName = input("输入年龄")
birthday = int(input("出生年月"))
age = datetime.date.today().year - birthday
print(age)