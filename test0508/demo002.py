# f=open('E:/workspace/datas/action.txt','rt')
# b=f.read()
#
# print(type(b))

# a=int(input("qingshuru第一个数"))
# b=int(input("diergeshu"))
# print(a/b2)


class person:
    name = 'lili'
    def get_name(self):
        return self.name

print(person.name)
p=person()
print(p.name)
print(p.get_name())

person.name='huahua'
print(person.name)
print(p.name)
print(p.get_name())