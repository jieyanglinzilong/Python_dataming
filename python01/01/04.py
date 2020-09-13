def run(mark):
    if (mark > 90):
        grade = "优秀"
    elif (mark > 70 and mark < 90):
        grade = "良好"
    elif (mark < 60):
        grade = "普通"
    return grade


a = run(int(input("输入分数")))
print(a)
if (a == '优秀'):
    print("优秀啊")
else: print("好菜")
