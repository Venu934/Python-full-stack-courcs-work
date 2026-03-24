# fee caliculator
def caliculate_fee(cource, marks):
    if cource == "AI":
        fee = 50000
    elif cource == "WEB-DEV":
        fee = 30000
    elif cource == "DATA-SCIENCE":
        fee = 40000
    else:
        return None # Invalid course
    if marks >=90:
        fee -= 5000
    return fee
def main():
    cource = input("Enter the course: ")
    marks = int(input("Enter the marks: "))
    fee = caliculate_fee(cource, marks)

    if fee is None:
        print("Invalid course selected.")
    else:
        print(f"The fee is {fee}.")
main()