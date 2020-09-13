import sys
fileName = sys.argv[0]
fileName = input("输入文件名: ")
line_no=0
f1 = open('agn.txt', 'w',encoding='utf8')
sys.stdout=f1
with open(fileName, 'r', encoding='utf8') as f:
    for line in f:
        line_no += 1

        print(line_no, ":", line)
sys.stdout = sys.__stdout__
print("done")
