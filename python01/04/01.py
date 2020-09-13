class gn:
    __name = 'cf'
    __kn = 'gn'

    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
p = gn('周')
print(p.name)
print(p.__name)

#print(p.__kn) #报错
