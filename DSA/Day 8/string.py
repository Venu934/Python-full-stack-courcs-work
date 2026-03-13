def count_chars(text):
    count = 0
    for char in text:
        count += 1
    return count
def main():
    text = input("Enter a string: ")
    print("Number of characters in the string: ", count_chars(text))
main()