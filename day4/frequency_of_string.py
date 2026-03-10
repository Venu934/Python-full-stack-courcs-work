string = "banana"
freq = {}
count = 0
for char in string:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1
print(freq)
    
