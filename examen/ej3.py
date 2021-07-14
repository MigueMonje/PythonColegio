bnum = int(input("Cuanto: "))
day = input("Hoy (h) o anterior (a): ")[0].lower()
ctv = 40 if day == "a" else 50
cst = (bnum * ctv) / 100
print(f"{bnum} Panes: {cst}Bs")