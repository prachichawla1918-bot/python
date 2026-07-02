class pay:
    def super(self):
        print("payment")
class upi(pay):
    def super(self):
        print("upi")
class bank(pay):
    def super(self):
        print("bank")
b=bank()
b.super()
u=upi()
u.super()
p=pay()
p.super()