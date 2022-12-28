archivo=open('C:\\Users\lautarofn\Downloads\input.txt','r')

inven_str=archivo.read()
inventario=inven_str.splitlines()

cal_elfos=[]
suma=0
for meal in inventario:
    if meal=='':
        cal_elfos.append(suma)
        suma=0
    else:
        suma=suma+int(meal)
    if meal==inventario[len(inventario)-1] and meal!='':
        cal_elfos.append(suma)

mayor=0
for elfo in cal_elfos:
    if elfo>mayor:
        mayor=elfo
print (mayor)

#print(cal_elfos)
