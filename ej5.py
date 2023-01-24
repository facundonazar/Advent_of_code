archivo=open('C:\\Users\lautarofn\Documents\GitHub\Advent_of_code\ej5-input.txt','r')
txt=archivo.read()
all=txt.splitlines()

movimientos=[]
for line in all:
    if 'move' in line:
        movimientos.append(line)

posiciones=[]
for line in all:
    if str(line)=='':
        break
    else:
        posiciones.append(line)

posiciones_rev=posiciones.copy()
posiciones_rev.reverse()
posiciones_rev.pop(0)

listas_posiciones=[]
magic_number=4

for x in range(8):
    listas_posiciones.append([])
    contador=0
    contador2=3
    while contador<35:
        listas_posiciones[x].append(posiciones_rev[x][int(contador):int(contador2)])
        contador+=magic_number
        contador2+=magic_number

for x in movimientos:
    print(x)
    nums=[]
    for y in x:
        if y.isnumeric():
            nums.append(int(y))
    cant=int(nums[0]-1)
    print('cant=',cant)
    origen=int(nums[1]-1)
    print('origen=',origen)
    destino=int(nums[2]-1)
    print('destino=',destino)
    
    for z in (0,cant):
        print(z,'° de cant(',cant,')')
        aux='   '
        helper=1
        while aux=='   ':
            aux=listas_posiciones[len(listas_posiciones)-helper][origen]
            print('aux=',aux)
            if aux=='   ':
                helper=helper+1
                print(helper)
            else:
                print(listas_posiciones[len(listas_posiciones)-helper][origen])
                listas_posiciones[len(listas_posiciones)-helper][origen]='   '
                print('se hizo el pop')

        aux_drop='   '
        helper_drop=1
        cont=0
        while aux_drop=='   ':
            cont=+1
            aux_drop=listas_posiciones[len(listas_posiciones)-helper_drop][destino]
            print('aux_drop=',aux_drop)
            if aux_drop=='   ':
                helper_drop=helper_drop+1
                print(helper_drop)
            elif len(listas_posiciones)-helper_drop+1==len(listas_posiciones):
                listas_posiciones.append([])
                for c in range(9):
                    listas_posiciones[len(listas_posiciones)-1].append([])
                listas_posiciones[len(listas_posiciones)-1][destino]=aux
                print(listas_posiciones[len(listas_posiciones)-1][destino])
                print('se añade el aux')
            


#    listas_posiciones[int(destino)].append(listas_posiciones[int(origen)])
#    listas_posiciones.pop()


#print(listas_posiciones)