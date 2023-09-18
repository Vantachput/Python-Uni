from math import sqrt
print("Число"," ", "Квадратний корінь")
for elem in range(100,0,-1):
    if(sqrt(elem) == int(sqrt(elem))):
        print(" {elem:3} \t\x20\x20\x20\x20 {sqrt:3}".format(elem = elem, sqrt = int(sqrt(elem))))
  
