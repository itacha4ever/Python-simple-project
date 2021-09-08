wieght = float(input(' wieght is : '))
unite = input('(L)lbs or (K)g ')
if unite.upper() =="L":
   convert = wieght* 0.45
   print(f"u are {convert} Kilos")
else:
    convert = wieght / 0.45
    print(f"u are {convert} poend")




