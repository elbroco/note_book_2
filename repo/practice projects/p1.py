def per(a, b):
    A = ((b/a)-1)*100
    return A

main = float(input("curso inicial: "))
min = float(input("curso minimo: "))
ave = int(input("curso promedio: "))
max = int(input("curso maximo: "))


print("diferencia con curso minimo:", round(per(main,min),1),"%")
print("diferencia con curso promedio:", round(per(main,ave),1),"%")
print("diferencia con curso maximo:", round(per(main,max),1),"%")

