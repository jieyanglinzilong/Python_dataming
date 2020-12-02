import xlwt

filename = '../data/评分.txt'
excel = '各项评分.xls'
fopen = open(filename, 'r')

lines = fopen.readlines()
file = xlwt.Workbook(encoding='utf-8', style_compression=0)
#新建一个sheet
sheet = file.add_sheet('data')
i = 0
location = ""
service =""
fact = ""
health = ""
j=0
for line in lines:

    if i ==0:
        location=line
    if i == 1:
        fact=line
    if i ==2:
        service=line
    if i >=3:
        j+=1
        health = line
        sheet.write(j, 0, location)
        sheet.write(j, 1, fact)
        sheet.write(j, 2, service)
        sheet.write(j, 3,health)
        line = line.strip('\n')

        i=0
    i+=1


file.save(excel)

