
# ---------------- frozenset properties -----------------
# duplicate not allowed
# hetrogeneous
# in frozenset({})
# immumutable
# indexing not allowed
# insertaion order not preserved

set1 = {10,25,35,10,100}
list1 = [100,250,350,100]
print(set1)
fs1 = frozenset(set1)
fs2 = frozenset(list1)
print(fs1)
print(fs2)

print(len(fs1))

print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1)

# we cant perform any manipulation on frozenset since it is immutable

