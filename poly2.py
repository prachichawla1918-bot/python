class animal:
    def sound(self):
        print("Animal sound")

class dog(animal):
    def sound(self,name):
        self.name=name
        print(f"name of dog is{self.name}")

d=dog()
d.sound("sheru")

A=animal()
A.sound()
