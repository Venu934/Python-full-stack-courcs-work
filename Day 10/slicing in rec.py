def display(s,i):
    if i == len(s):
        return
    print(s[:i+1])
    display(s,i+1)
    print(s[:i+1])
    
display("python programing",0)
