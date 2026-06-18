m1=int(input("enter the marks of hindi"))
m2=int(input("enter the marks of maths"))
m3=int(input("enter the marks of english"))
m4=int(input("enter the marks of marathi"))
m5=int(input("enter the marks of science"))

percentage=m1+m2+m3+m4+m5/5
print("Percenatge:",percentage)

if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
    print("failed in subject")

elif percentage>=75:
    print("first class with distinction")

elif percentage>=60 and percentage<75:
    print("first class")

elif percentage >= 50 and percentage<60:
    print("second class")

elif percentage >= 35 and percentage<50:
    print("Pass")

else:
    print("Fail")
