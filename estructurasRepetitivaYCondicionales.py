""" Ejercicios estructuras repetitivas y estructuras condicionales.
1. Realice un programa que lea 4 números y diga cuántos son pares y
cuantos impares y devuelva la sumatoria de los pares.
"""

numeros=[1,2,3,4]
pares=[]
suma=0
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
        suma+=i
print(f'Los pares son {pares} y la suma de ellos fue: {suma}')

"2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo"
        
diezNumeros=[555,86,133,22,254,-87,753,22,51,91]
menorNumero=diezNumeros[0]
mayorNumero=diezNumeros[0]
qMayoresDeCien=0


for i in diezNumeros:
    if i >100:
        qMayoresDeCien+=1
    if i < menorNumero:
        menorNumero=i
    if i > mayorNumero:
        mayorNumero=i
qMenoresDeCien=10-qMayoresDeCien        
print(f"El menor numero de estos 10 analizados es el {menorNumero}, el mayor es el {mayorNumero} , los numeros superiores a cien son {qMayoresDeCien} y los menores a cien {qMenoresDeCien}")

""" 
3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son
mujeres, cuántos varones, cuántos mayores de edad y cuántos
menores de edad. """

edades=[]
sexo=[]

for i in range(15):
    bandera=False
    
    #Aca validamos que la edad se encuentre en un rago entre 0 y 150
    while bandera is False:
        edad=int(input("Ingrese su edad: "))
        if edad >=0 and edad <=150 :
            edades.append(edad)
            bandera is True
            break

        else:
            print("Edad incorrecta - Debe ingresar una edad válida entre 0 y 150.")
    while bandera is False:
        sex=input("Ingrese su Sexo M o F: ")
        sex=sex.upper()
        if sex== "M" or sex == "F":
            sexo.append(sex)
            bandera is True
            break

        else:
            print("Ingrese para Masculino la letra M o para Femenino la letra F")        

print( f'las edades de las {len(edades)} personas analizadas son:{edades}')
print( f'el sexo de las {len(sexo)} personas analizadas son:{sexo}')

#Reciclo codigo utilizado arriba


menorNumero=edades[0]
mayorNumero=edades[0]


for i in edades:
    if i < menorNumero:
        menorNumero=i
    if i > mayorNumero:
        mayorNumero=i       
print(f"El menor numero de estos {len(edades)} analizados es el {menorNumero}menor numero y mayor numero es {mayor mayorNumero} ")


"""4. Leer 10 números y mostrar solamente los números positivos, y su
sumatoria."""

number=[-8,7,65,-78,74,1,-3,45,63,78]
numberPositive=[]
addNumberPositive=0
for i in number:
    if i>0:
        numberPositive.append(i)
        addNumberPositive+=i
print(f'Los numeros positivos son los siguientes. {numberPositive} y su sumatoria da: {addNumberPositive}')


""""5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos
números. """

number=[-8,-7,-65,-78,-74,-1,-3,-45,-63,-78,-65,-22,-1,-44,-89]
numberPositive=[]
for i in number:
   i=i*-1
   numberPositive.append(i)
print(f'Los numeros positivos son los siguientes. {numberPositive}')