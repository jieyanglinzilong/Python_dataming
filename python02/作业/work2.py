from random import randrange, choice

n = 9
nextlist = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5, 7), (2, 4, 8), (3, 7), (6, 4, 8), (7, 5)]
p = randrange(0, n)
print(type(p))
position = [0] * 9
position[p] = 1
print(position)
for i in range(0, 10):
    i += 1
    n -= 1
    a=1
    while a==1:
     x, y, z = map(eval, input('输入三个打开的洞口:').split())
     if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
         break
     print("输入错误请重新输入")
    x = x - 1
    y = y - 1
    z = z - 1
    if position[x] == 1 or position[z] == 1 or position[y] == 1:
        print("成功")
        break
    else:
        print("没有找到继续")
        position[p] = 0
        newposition = choice(nextlist[p])
        p = newposition
        position[p] = 1
        print(position)

else:
    print("超过上限")