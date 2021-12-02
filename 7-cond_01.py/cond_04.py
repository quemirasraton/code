
edad: int = 121 #Años

is_baby:  bool = (0 <= edad <= 1)
is_child: bool = (2 <= edad <= 6)
is_adult: bool = (6 <= edad <= 90)
is_elder: bool = (91 <= edad <= 120)

if is_baby:
    print("Regalar pañales")
elif is_child:
    print("Regalar pelota")
elif is_adult:
    print("Regalar ropa")
elif is_elder:
    print("Regalar pañales")
else:
    print("Felicitale!")
    