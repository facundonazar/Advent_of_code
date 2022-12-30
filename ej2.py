archivo=open('C:\\Users\lautarofn\Documents\GitHub\Advent_of_code\ej2-input.txt','r')
guide=archivo.read()

s_guide=guide.splitlines()

#print(s_guide)

split_s_guide=[]
for round in s_guide:
    split_s_guide.append(round.split())

score=0
for round in split_s_guide:
    if round[0] == 'A':
        score += 1
    elif round[0] == 'B':
        score += 2
    elif round[0] == 'C':
        score += 3

    if round[0] == 'A' and round[1] == 'X':
        score += 3
    elif round[0] == 'A' and round[1] == 'Y':
        score += 0
    elif round[0] == 'A' and round[1] == 'Z':
        score += 6

    if round[0] == 'B' and round[1] == 'Y':
        score += 3
    elif round[0] == 'B' and round[1] == 'Z':
        score += 0
    elif round[0] == 'B' and round[1] == 'X':
        score += 6

    if round[0] == 'C' and round[1] == 'Z':
        score += 3
    elif round[0] == 'C' and round[1] == 'X':
        score += 0
    elif round[0] == 'C' and round[1] == 'Y':
        score += 6

print (score)
print(len(split_s_guide))
