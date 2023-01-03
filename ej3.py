import string

a=list(string.ascii_lowercase)
A=list(string.ascii_uppercase)

archivo=open('C:\\Users\lautarofn\Documents\GitHub\Advent_of_code\ej3-input.txt','r')
archivo_str=archivo.read()
rucksacks_list=archivo_str.splitlines()
sum_contador=0
priority_list=a+A

print(len(rucksacks_list))

for line in rucksacks_list:
    lenght1=len(line)//2
    lenght2=lenght1+1
    line_mitad1=line[:lenght1]
    line_mitad2=line[lenght2:]
    for letra in line_mitad1:
        if letra in line_mitad2:
            print(letra)
            contador=0
            for x in priority_list:
                contador+=1
                if letra == x:
                    print(letra, x,contador)
                    sum_contador+=contador
print(sum_contador)
    