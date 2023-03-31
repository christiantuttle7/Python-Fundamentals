eng2sp = {} # or
eng2sp1 = dict() # These lines create an emptydictionary object

eng2sp['one'] = 'Uno'
eng2sp["two"] = "dos"
eng2sp["three"] = "tres"
eng2sp[4] = "quatro"
eng2sp["five"] = "sinco"

print(eng2sp)

print(eng2sp['one'])
eng2sp['one'] = 'something else'

print(eng2sp)

print(eng2sp.get('one'))
print(eng2sp)

print(list(eng2sp.keys()))

for k in eng2sp:
    print('key = {}, value = {}'.format(k, eng2sp.get(k)))
    print('key = {}, value = {}'.format(k, eng2sp[k]))

