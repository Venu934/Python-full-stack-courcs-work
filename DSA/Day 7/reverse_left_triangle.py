# n = 5
# for i in range(1,n):
#     print("@ "*i)
# n = 5
# for i in range(n, 0, -1):
#     print("@ "*i)

# n = 5
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
n  = 5
num = 1
for i in range(1, n):
    for j in range(1, i+1):
        print(j, end=" ")
        num += 1
    
    print()




