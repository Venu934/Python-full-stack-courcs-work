''' def display(s,i):
    if i <=0 :
        return
    
    display(s,i-1)
    print(s*i)
    
display("abc",5)
'''
'''
def display(s,i,n):
    if i == len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)

display("abcdefgh",0,2)

'''
'''
def display(s,i,sum):
    if i == len(s):
        return sum
    return display(s,i+1,sum+s[i])
print(display(['python','c','c++'],0,''))

def display(s,i,sum):
    if i == len(s):
        return sum
    return display(s,i+1,sum+s[i])
print(display([1,2,3,4,5,6,7,8],0,0))
'''
#pass by value
def display(n):
    n = n+10
    print("Inside:",n)
n = 10.3
display(n)
print("outside",n)


def display(n):
    n = n+[6,7]
    print("Inside:",n)
n = [1,2,3,4,5]
display(n)
print("outside",n)



def pass_by_reference(lst):
    print("Before change inside function:", lst)
    lst.append(100)
    print("After change inside function:", lst)

numbers = [1, 2, 3]
pass_by_reference(numbers)

print("Outside function:", numbers)


def modify_dict(d):
    d["age"] = 25
    print("Inside function:", d)

person = {"name": "John"}
modify_dict(person)

print("Outside function:", person)


#pass by value tuple is immutable
def modify_tuple(t):
    t = t + (4,)   # creates new tuple
    print("Inside function:", t)

nums = (1, 2, 3)
modify_tuple(nums)

print("Outside function:", nums)





    
    

