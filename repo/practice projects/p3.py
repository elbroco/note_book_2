def per(a, b):
    A = (10/a)*b
    return A

main = float(input("curso inicial: "))
min = float(input("curso minimo: "))
ave = int(input("curso promedio: "))
max = int(input("curso maximo: "))


print("diferencia con curso minimo:", round(per(main,min),1),' horas')
print("diferencia con curso promedio:", round(per(main,ave),1),' horas')
print("diferencia con curso maximo:", round(per(main,max),1),' horas')
