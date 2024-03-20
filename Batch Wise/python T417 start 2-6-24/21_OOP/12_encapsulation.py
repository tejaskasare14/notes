class Hero:
   heroname = "salman"
   _paisa = "20 Lakh" #protected
   __gf = "katrina kaif" #private
   
   def _a(self):
      print("hello a")
      print(Hero.__gf)
   def __b(self):
      print("hello b")
   
class Heroin(Hero):
   pass

class Villain:
   pass

h = Heroin()
print(h.heroname)
print(h._paisa)
#print(h.__gf)
h._a()
#h.__b()

