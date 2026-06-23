# def calculate_bill(units,rate=8):
#     bill=units*rate
#     return bill

# units=int(input("enter units consumed:"))
# print("total bill:",calculate_bill(units))

def validate_email(email):
    return '@'in email
def validate_password(password):
    return len(password) >=6
def generate_hash(password):
    return "*" * len(password)
def register_user(name,email,password):
    if validate_email(email)and validate_password(password):
        print("user registered successfully")
    else:
        print("invalid email or password")  
register_user("prachi","prachi@gmail.com","123456")  

