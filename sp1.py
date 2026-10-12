#13
#12.10
#program kouli kulicku
import time
import math
pocet = 10
print("Koulicka se kouli!")
for i in range (pocet):
    print(" "*i + "O")
    time.sleep(0.1)
for i in range (pocet-1):
    print(" "* (pocet-i) + "O")
    time.sleep(0.1)
print("tabulka")
for i in range (1, pocet+1):
    print(i, i*i, math.sqrt(i))