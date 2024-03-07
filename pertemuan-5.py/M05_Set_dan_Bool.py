print("\033c")

Set_1 = {"Toyota", "Daihatsu", "Honda"}
Set_2 = set(("Toyota", "Daihatsu", "Honda"))

print("Tipe data Set_1 adalah", type(Set_1))
print("Tipe data Set_2 adalah", type(Set_2))
print("Data Set_1:", Set_1)
print("Data Set_2:", Set_2)
print("============================")

for x in Set_1:
    print(x)
print("============================")

print(len(Set_1))

if "Daihatsu" in Set_1:
    print("Yes 'Daihatsu' is an item in Set_1.")

# Add an item
Set_1.add("Mitsubishi")
print(Set_1)

# Add multiple items
Set_1.update(["Suzuki", "Mazda", "Nissan"])
print(Set_1)

print()
print()
print("Part 2")
print("============================")

Set_1.remove("Honda")
print(Set_1)

Set_1.discard("Mazda")
print(Set_1)

Set_1.pop()
print(Set_1)

Set_1.clear()
print(Set_1)

del Set_1
print("============================")

# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print("============================")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

print()
print()
print("Part 2")
print("============================")
# Tipe data boolena
print("Case 1")
# tipe data boolean yang kit  deklarasikan dengan cara standar
f = bool(True)
g = bool(False)
print(f)
print(g)
print("=====================================")

print("Case 2")
# tipe data boolean yang kita deklarasikan dengan cara lain
print(3 > 2)
print(3 + 2 == 5)
print(3 < 2)
print("=====================================")

print("Case 3")
# tipe data boolean yang kita deklarasikan dengan cara lain
penghasilan = 20000000
penghasilanTanpaPajak = 4000000
if penghasilanTanpaPajak > 3000000:
    print(True)
else:
    print(False)

if penghasilan > 3000000:
    print(True)
else:
    print(False)
print("=====================================")

print("Case 4")
# tipe data boolean yang kita deklarasikan dengan cara lain
# semua data tidaknol
a = 3
b = "Ini data string."
c = [1, 2, 3]
d = (1, 2, 3)
e = {"nama": "Budi", "umur": 30}

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("=====================================")

#PART 3
#Case 5
print("Case 5")
#Variabel yang kosong memiliki nilai Boolean False
a = 0                                          #integer null
b = ""                                         #string kosong
c = ()                                         #tuple kosong
d = []                                         #list kosong
e = {}                                         #dictionary/set kosong
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("================================")

#Case 6
print("Case 6")
#Variabel yang panjangnya nol memiliki nilai Boolean False 
class myClass():
    def __len__(self):
        return 0 

print(bool(myClass()))
print("================================")
