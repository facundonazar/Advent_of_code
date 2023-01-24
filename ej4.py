archivo=open('C:\\Users\lautarofn\Documents\GitHub\Advent_of_code\ej4-input.txt','r')
guide=archivo.read()
s_guide=guide.splitlines()

pares_regiones=[]

for region in s_guide:
    pares_juntos=region.split(', ')
    pares_regiones.append(pares_juntos)

contador=0

for par in pares_regiones:
    text=str(par)
    s1,s2,s3=text.partition(',')
    s1=s1[2:]
    s3=s3[:len(s3)-2]  
    s1a,s1b,s1c=s1.partition('-')
    s2a,s2b,s2c=s3.partition('-')
    
    if all (item in list(range(int(s1a),int(s1c))) for item in list(range(int(s2a),int(s2c)))):
        contador+=1
    elif all (item in list(range(int(s2a),int(s2c))) for item in list(range(int(s1a),int(s1c)))):
        contador+=1

print(contador)

