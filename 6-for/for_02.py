
#--------------------------------------------------- 
names_list: list[str] = ["Jhon", "Mary", "Lucy"]

name1: str = input()
names_list.append(name1)

name2: str = input()
names_list.append(name2)

name3: str = input()
names_list.append(name3)

for name  in names_list:
    print(f"Hola {name}")

names_list_reversed: list[str] = list(reversed(names_list))

for name in names_list_reversed:
    print(f"Hola {name}")

#--------------------------------------------------- 