import math
def hcf_(x, y):
    smaller = min(x,y)
    for i in range(1,smaller+1):
        if (x % i == 0 ) and (y % i == 0):
            hcf = smaller
            break
    return hcf
x = 6
y = 3
print(hcf_(x,y))
