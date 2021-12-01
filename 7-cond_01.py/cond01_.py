#Conditionals

num_list: list[int] = [0, 1, 2, 3, 4, 5]

if (len(num_list) >= 4):                                  
    print("Hay 4 o mas elementos! Voy a imprimirlos.")
    print(num_list)                                      # O se ejecuta uno o se ejecuta otro
else:
    print("Hay menos de 4 elementos, pon mas porfavor.")