class person:
    theatre="PVR cinema"
    def __init__(self,name):
        self.name=name
    def display(self):
        print("name:",self.name)

class Booking(person):
    ticket_price=200
    def __init__(self,name,movie,tickets):
        super().__init__(name)
        self.movie=movie
        self.tickets=tickets

    def display(self):
        print("\n---Booking details---")
        print("theatre:",person.theatre)
        print("customer:",self.name)
        print("movie:",self.movie)
        print("tickets",self.tickets)

class VIPBooking(Booking):

    ticket_price = 350

    def display(self):
        total = self.tickets * VIPBooking.ticket_price

        print("\n----- VIP Booking -----")
        print("Theatre :", person.theatre)
        print("Customer :", self.name)
        print("Movie :", self.movie)
        print("VIP Tickets :", self.tickets)
        print("Ticket Price : ₹", VIPBooking.ticket_price)
        print("Total Bill : ₹", total)


name=input("enter customer name:")

print("\n--movies--")
print("1.kalki")
print("2.pushpa2")
print("3.saiyaara")

choice=int(input("Enter choice(1-3):"))

if choice == 1:
    movie="kalki"

if choice == 2:
    movie="pushpa2"

if choice == 3:
    movie="saiyaara"

tickets=int(input("enter number of ticket:"))
print("\n---booking type---")
print("1.normal")
print("2.VIP")

book=int(input("enter choice:"))

if book ==1:
        b = Booking(name, movie, tickets)
else:
        b = VIPBooking(name, movie, tickets)

bookings= [b]

print("\n========== MOVIE TICKET ==========")

for i in bookings:
    i.display()

print("\nThank You! Visit Again.")