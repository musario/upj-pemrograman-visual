print("/033c")

Set_1 = {"Samsung", "Vivo", "Xiaomi"}
Set_2 = set(("Advan", "Iphone", "Oppo"))

print("Tipe data Set_1 adalah", type(Set_1))
print("Tipe data Set_2 adalah", type(Set_2))
print("Data Set_1:", Set_1)
print("Data Set_2:", Set_2)
print("============================")

for x in Set_1:
    print(x)
print("============================")

print(len(Set_1))

if "Iphone" in Set_1:
    print("Yes 'Iphone' is an item in Set_1.")

# Add an item
Set_1.add("Huawei")
print(Set_1)

# Add multiple items
Set_1.update(["Nokia", "Sony", "LG"])
print(Set_1)
