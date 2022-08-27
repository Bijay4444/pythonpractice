weight = int(input("Weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converter = weight* 0.45
    print(f"you are {converter} kilogram")
else:
    converter = weight / 0.45
    print(f"you are {converter} pounds")