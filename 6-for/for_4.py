
#-----------------------------------------
#Recorrer una lista de nombres mostrando su indice dentro de la lista

names_list: list[str] = ["name1", 'name2', "name3"]

for name in names_list:
    position: int = names_list.index(name)
    print("{position}""{name}")