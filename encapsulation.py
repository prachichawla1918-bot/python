class student:
    def __init__(self):
        self.name="radha"
        self.age=19

s= student()
print(s.name)
print(s.age)

#new code using private variable
class student:
    def __init__(self):
        self.name="radha"
        self.__age=19
    def edit(self,age):
        self.__age=age
    def show(self):
        print(self.__age)
s=student()
s.edit(55)
print(self.__age)