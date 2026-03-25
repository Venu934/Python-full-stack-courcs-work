def display(n):
    if n>10:
        return
    print("before",n)
    display(n+1)
    print("after",n)
display(1)


