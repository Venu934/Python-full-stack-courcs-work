s1 = "silent"
s2 = "listens"

freq1 = {}
freq2 = {}

# Build frequency dictionary for s1
for char in s1:
    if char in freq1:
        freq1[char] += 1
    else:
        freq1[char] = 1

# Build frequency dictionary for s2
for char in s2:
    if char in freq2:
        freq2[char] += 1
    else:
        freq2[char] = 1

# Compare the two frequency dictionaries
if freq1 == freq2:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
