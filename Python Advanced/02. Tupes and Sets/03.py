l = [{"a": 0}]
ll = [x for x in l]

print(id(l))
print(l)
print(id(ll))
print(ll)

ll.append({"b": 0})

print(id(l))
print(l)
print(id(ll))
print(ll)
