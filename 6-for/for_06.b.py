# 7. Recorrer una lista 
#
# -range() always return an itnerator.
# You must convert it to a list manually.
# -range() function can be called with up three parameters.


name_list:  list[str]   = ["Jhon", "Mary", "Lucy"]
index_list: list[int]   = list(range(len(name_list))) 
new_list_1: list[str]   = []
new_list_2: list[str]   = []

for name in name_list:
    new_list_1.append(name)

print(new_list_1)

for name in name_list:
    new_list_2 = new_list_2 + [name]

print(new_list_2)

print(new_list_2 == new_list_1)

for index in index_list:
    print(f"Index: {index}")
    
# 1. One Parameter
print(list(range(5))) # Excludes last number

# 2. Two Parameter
print(list(range(3, 6))) # Excludes last number

# 3. Tree Parameters
print(list(range(1, 11, )))
