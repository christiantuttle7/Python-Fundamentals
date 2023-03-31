new_set = set()

print(new_set)

for i in range(1,14,3):
    new_set.add(i)

print(new_set)

new_set.add(1)
print(new_set)

new_set.pop()
print(new_set)

print(13 in new_set)

new_set.remove(13)

print(new_set)