
#------------------------------------------
name_list: list[str] = []

for name in name_list:
    print(f"Hello {name}")

for 1 in range(3):
    name: str = input(f"Escribe nombre:\t")
    name_list.append(name)

print(f"\n")

for name in reversed(name_list):
    print(f"Hello {name}")

#-----------------------------------------
number_list: list[str] =[]


for 1 in range(3):
    number: float = float(input(f"Put a number:\t"))
    number_list.append(number)

for number in number_list:
    print(number)
    
