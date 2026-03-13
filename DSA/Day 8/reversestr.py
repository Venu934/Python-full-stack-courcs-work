def rev_text(text):
    rev= ""
    for char in text:
        rev = char + rev
    return rev
def main():
    text = input("Enter a string: ")
    print("Reversed string: ", rev_text(text))
main()