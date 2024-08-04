phrase = str(input("coloca la frase"))
my_list = phrase.split(" ")

ci = len(my_list)
print(ci)

time = ci/2

print(time,'segundos')
print('numero de palabras',str(ci))

if time >= 60:
    print('mucho texto, crack')
else:
    print('alrighty')

time2 = time * (7/10)

print('i would say it in ',str(time2),' seconds')