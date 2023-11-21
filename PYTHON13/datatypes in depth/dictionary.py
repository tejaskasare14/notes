# to store data in key value pair - use dict
marks = {"java":95,"python":96,"adjango":95}
print(marks)
#here "java" is key and 95 is value

# ---------------- dict properties -----------------
# duplicate key are not allowed, value can be duplicate
# hetrogeneous
# in {}
# mutable
# indexing not allowed, since we use key for manipuation
# insertaion order preserved

# ---------------- how to crerate a dict -----------------
# empty dict
dict1 = {}
print(dict1)
print(type(dict1))

dict2 = dict()
print(dict2)
print(type(dict2))

#if we know emelents
marks = {"java":95,"python":96,"adjango":95}
student = {1:"aniket",2:"raj"}
print(marks)
print(student)

# by using list of tuple
food=[("day1","veg"),("day2","non-veg"),("day3","jain food")]
food_dic = dict(food)
print(food_dic)

# add,update,delete dict elements
print("---adding elemets to dict -----")
alphabates = {"a":"apple"}
print(alphabates)
alphabates['b'] = "banana"
alphabates['c'] = "chiku"
print(alphabates)

print("---accessing elemets of dict -----")
print(alphabates['a'])
#print(alphabates['d']) #KEY ERROR

print("---updating elemets of dict -----")
print(alphabates)
alphabates['a'] = "avacado" #since  "a" key is present, it will update apple to avacado
print(alphabates)

alphabates['d'] = "dragonfruit" #since  "d" key is not present, it will add new key value pair
print(alphabates)

print("---delete elemets of dict -----")
del alphabates['a']
print(alphabates)

#del alphabates['e'] # KEYERROR

# dict built in functions
print("--- dict built in functions ----------")
marks = {"java":95,"python":96,"adjango":95}

print(len(marks))

print(marks.get("java")) #95
print(marks.get("angular")) #None

print(marks.keys())

print(marks.values())

print(marks.items())

print()
marks.pop("java")
print(marks)

#marks.pop("angular") #KEY ERROR

marks.popitem()
print(marks)

# {}.popitem() ERROR since dict is empty
marks.setdefault("python",99) #if given key alredy present tyhen it will not update the key
print(marks)

marks.setdefault("spring",99)
print(marks)

# adding one dict into another
d1 = {"p1":30,"p2":35}
d2 = {"p3":40,"p5":45}
# print(d1+d2) ERROR
print(d1)
d1.update(d2)
print(d1)


#what if dict has duplicate keys

d  = {"java":95,"angular":98,"java":99}
print(d.get("java"))










