#single : one parent class and on child class
#multilevel : level of parent and child class
#multiple : mutiple parent one child
#heirarchical : one parent multple child
#hybrid  : mix of any of above

#single : one parent class and on child class
'''
class P:
   pass
class C(P):
   pass 
'''

#multilevel : level of parent and child class
'''
class GP:
   pass
class P(GP):
   pass
class C(P):
   pass
'''

#multiple : mutiple parent one child
'''
class P1:
   pass
class P2:
   pass
class C(P1,P2):
   pass
'''

#heirarchical : one parent multple child
'''
class P:
   pass
class C1(P):
   pass
class C2(P):
   pass
'''

#hybrid  : mix of any of above
'''
class GP:
   pass
class P(GP):
   pass
class C1(P):
   pass
class C2(P):
   pass
'''

#Prgram on SI:
'''
class P:
   pdata = 10
   
class C(P):
   cdata = 20 
   
c = C()
print(c.pdata)
print(c.cdata)
'''

#program on MLI
'''
class GP:
   gpdata = 11
   data = 10
class P(GP):
   pdata = 22
   #data = 20
class C(P):
   cdata = 33
   #data = 30
c = C()
print(c.gpdata)
print(c.pdata)
print(c.cdata)
print(c.data)
'''

#Program on MI
'''
class P1:
   p1data = 100
   data = 199  
class P2:
   p2data = 200
   data = 299
   
class C(P1,P2):
   cdata = 300

c = C()
print(c.p1data)
print(c.p2data)
print(c.cdata)
print(c.data)
'''

#heirarchical : one parent multple child
'''
class P:
   pdata = 99
class C1(P):
   c1data = 199
class C2(P):
   c2data = 299

c1 = C1()
print(c1.pdata)
print(c1.c1data)
c2 = C2()
print(c2.pdata)
print(c2.c2data)
'''


#hybrid  : mix of any of above

class GP:
   gpdata = 55
class P(GP):
   pdata = 66
class C1(P):
   c1data = 33
class C2(P):
   c2data = 333
   
c1 = C1()
print(c1.gpdata, c1.pdata, c1.c1data)
c2 = C2()
print(c2.gpdata, c2.pdata, c2.c2data)



