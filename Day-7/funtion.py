# def wish(name):
#     print(f"Hello, {name}! Welcome to python 100 days of programming.")
# wish("Teja")
# #argument
# def display(username, email, password):
#     print(f"Usename: {username}")
#     print(f"Email: {email}")
#     print(f"password: {password}")
# display('ramesh', 'ramesh@gmail.com', 'ramesh123')
# display('suresh', 'suresh@gmail.com', 'suresh123')
#keyword argument
#phone number is default argument
# 


def display(*name):
    print("names: ", name)
display("Teja", "Ramesh", "Suresh")