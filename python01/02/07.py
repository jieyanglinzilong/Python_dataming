import sys
fileName = sys.argv[0]
f = open(fileName, 'r', encoding='utf8')
line_no = 0
while True:
    line_no+=1
    line = f.readline()
    if  line:
        print(line_no, ":", line)
    else:
        break
f.close()