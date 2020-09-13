#冒泡排序
def bubblesort(a):
    for i in range(len(a)-1,-1,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
def main():
 a=[9,30,70,80,74,96]
 bubblesort(a)
 print(a)
if __name__ == '__main__': main()
