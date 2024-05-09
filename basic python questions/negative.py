lst = [-1,-2,5,-2,45,-45]
pos = []
neg = []
for i in lst:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
print(F"positive number is {pos}")
print(f" negative number is{neg}")

