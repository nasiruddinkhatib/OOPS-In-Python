from main_abstraction import *

# Creating objects and testing the functionality
b = Bike("2", "Blue")
b.start()      # ✅ Output: Start with Kick
b.display()    # ✅ Output: Blue is the color of the bike.

s = Scooty("Honda Activa")
s.start()      # ✅ Output: Start with Self

c = Car("BMW", 6)
c.start()      # ✅ Output: Start with Key
