import pprint

with open('mat1.txt') as f1:
    a = f1.readline()
    mat1 = [list(map(str, row.split())) for row in f1.readlines()]
    mat1_F = a.split()
print("Первый автомат:")
pprint.pprint(mat1)
print("Хорошие состояния первого автомата:")
pprint.pprint(mat1_F)

with open('mat2.txt') as f2:
    b = f2.readline()
    mat2 = [list(map(str, row.split())) for row in f2.readlines()]
    mat2_F = b.split()

print("Второй автомат:")
pprint.pprint(mat2)
print("Хорошие состояния Второго автомата:")
pprint.pprint(mat2_F)
i1 = 0
i2 = 0

mat3 = [['0' for r in range(len(mat1[0]))] for d in range(len(mat2)*len(mat1))]


for l in range(len(mat1)):
    i1 = 0
    for i in range(len(mat2)):
        i=i+(l*4)
        for j in range(len(mat3[0])):
            mat3[i][j] = mat1[l][j]+ mat2[i1][j]
        i1 += 1

print("К3: К1 U K2")
pprint.pprint(mat3)

mat3_F = []
for l in range(len(mat1_F)):
    for i in range(len(mat2)):
        mat3_F.append(mat1_F[l]+str(i))
        mat3_F.append(str(i)+mat2_F[l])

mat3_F = list(set(mat3_F))
print("Хорошие состояния нового автомата K3:")
pprint.pprint(mat3_F)
stroka = ""
for i in range(len(mat3)):
    for j in range(len(mat3[0])):
        stroka += mat3[i][j] + ','

dost = list(set(stroka.split(',')))
dost.remove('')
print("Достижимые состояния нового автомата K3:")
print(dost)

mat3_FF = []
for i in range(len(mat3_F)):
    for j in range(len(dost)):
        if mat3_F[i] == dost[j]:
            mat3_FF.append(mat3_F[i])

print("Хорошие достижимые состояния нового автомата K3:")
pprint.pprint(mat3_FF)

F4 = []
for i in range(len(mat1_F)):
    for j in range(len(mat1_F)):
        F4.append(mat1_F[i]+mat2_F[j])
print("Хорошие состояния нового автомата K4:")
print("K4: K1 ∩ K2")
pprint.pprint(F4)
F4F = []
for i in range(len(F4)):
    for j in range(len(dost)):
        if F4[i] == dost[j]:
            F4F.append(F4[i])

print("Хорошие достижимые состояния нового автомата K4:")
pprint.pprint(F4F)