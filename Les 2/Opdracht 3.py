# Schrijf booleaanse expressies die van de variabelen van Practice Exercise 1_3 evalueren of:
# 1. 6.75 groter is dan a en kleiner b.
# 2. de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam.
# 3. de lijst inventaris leeg is, of juist meer dan 10 items bevat.

a = 6
b = 7
inventaris = ('papier','nietjes','pennen')
mijnNaam = ['Wesley Fakkeldij']
print (6.75 > a and 6.75 < b)

print (len (inventaris)>5*len(mijnNaam))

print (len (inventaris)==0 or len(inventaris)>10)

