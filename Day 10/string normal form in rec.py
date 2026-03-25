def display(s,i):
    if i == len(s):
        return
    print(s[i],end=' ')
    display(s,i+1)
    print()
    print(s[i],end=' ')

display("python programing", 0)
