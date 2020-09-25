a = float(input("请输入有固定收入的党员工资收入: "))
b = 0
if(a<=400):
    b = a*0.005
elif (a<600 and a>=401):
    b= a*0.01
elif (a>=601 and a<=800):
    b = a*0.015
elif (a<=1500 and a>=801):
    b= a*0.02
else :
    b = a*0.03
print(str.format("月工资收入为{0}元, 缴纳党费{1}元",a,b))

