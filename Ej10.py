alumnos_arch = open('nombres_1.txt', 'r',encoding='utf-8')
nota1_arch = open('eval1.txt', 'r',encoding='utf-8')
nota2_arch = open('eval2.txt', 'r',encoding='utf-8')


alumnos = alumnos_arch.read().split()
nota1 = nota1_arch.read().split()
nota2 = nota2_arch.read().split()


total_notas = {}
promedio = 0

for nombres_1, eval1, eval2 in zip(alumnos, nota1, nota2):
    total_notas[nombres_1.strip('\n,\' ')] = (int(eval1.strip('\n, ')) + int(eval2.strip('\n, ')))

for nombre in total_notas:
    promedio+=  total_notas[nombre]


promedio = promedio / len(total_notas)

print('alumnos que obtuvieron menos que el promedio: ')
for nombre in total_notas:
    if total_notas[nombre] < promedio:
        print(nombre)


alumnos_arch.close
nota1_arch.close
nota2_arch.close

