def per(a, b):
    A = ((b/a)-1)*100
    return A

main = float(input("curso inicial: "))
min = float(input("crudo inicial: "))
ave = int(input("curso promedio: "))
max = int(input("crudo promedio: "))


print("reduccion de material inservible en el curso inicial es de:", round(per(main,min),1),"%")
print("reduccion de material inservible en el curso promedio es de::", round(per(ave,max),1),"%")

