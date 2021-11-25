
name_list:  list[str]   = ["Jhon", "Mary", "Lucy"]
new_list_1: list[str]   = []
new_list_2: list[str]   = []

for name in name_list:
    new_list_1.append(name)

print(new_list_1)

for name in name_list:
    new_list_2 = new_list_2 + [name]

print(new_list_2)

print(new_list_2 == new_list_1)