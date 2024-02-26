marks = [95,96,92]
#to store data in key value pair, we need dictionary (dict)
#ex : makrs = {"python":95, "java":96, "sql":92}

#dict properties
#1. different data type
#2. indexing not allowed, instead we use key
#3. no limit on size
#4. duplicate keys are not allowed
#5. in {}
#6. mutable : we can perform chnages inside dict like, add remove elements etc

#creating a dictionary 
#empty dict
d1 = {}
print(type(d1))

#alresy known elements
marks = {"python":95, "java":96, "sql":92}
print(marks)
print(type(marks))

#accessing dict elements
print(marks['python'])

#from list of tuple
lt = [("python",95),("java",96),("sql",92)]
d3 = dict(lt)
print("dict from list of tuple : ", d3)

#add,update and delete dict elements
print("add,update and delete dict elements")
marks = {"python":95, "java":96, "sql":92}
print(marks)
#adding new element in dict
marks['djnago'] = 99 #adding new element in dict
print(marks)

#updating existing element in dict
marks['python'] = 98
print(marks)

#deleting existing element in dict
del marks['python']
print(marks)


#built in functions on python
fruits = {"a":"apple","b":"banana","c":"chiku"}
print(fruits['a'])
print(fruits.get('a')) #to access elements based on key
print(fruits.keys())   #to access all keys
print(fruits.values()) #to access all values
print(fruits.items())  #to access all elements/items

fruits.pop('a') #to remove element based on key
print(fruits)
#fruits.pop('z') #NameError: name 'z' is not defined

fruits.setdefault('d','dragonfruit') #add new key valu pair if specified key is not present
print(fruits)

fruits.setdefault('b','berry') #it will not add new key value pair since specified key is alredy present
print(fruits)

#what if duplicate key is present
fruits = {"a":"apple","b":"banana","c":"chiku","a":"aamba"}
print(fruits['a'])
