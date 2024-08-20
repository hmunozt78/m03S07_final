'''
Ejercicio Final Modulo 3 Sesion 7

Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:

• Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio 
de calificaciones sea superior a 85.

• Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años 
y cuya edad sea un número primo.
'''
from statistics import mean

def primo (a):
    contador = int(0)
    for x in range(2,a):
        if (a%x)==0: 
            contador+=1
            break
    if contador == 1: return(False)
    else: return(True)

estudiantes = [ 
                {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
                {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
                {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
                {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
                {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
               ]

for n in estudiantes:
    for clave, valor in n.items():
        promedio = round(mean(n.get("calificaciones")),1)
        edadPaso = n.get("edad")
        if (edadPaso<18) or (promedio<85) : 
            continue

        print(f'{clave} : {valor}')
        
        if ((n.get("edad"))>18):
            esPrimo=primo(n.get("edad"))
            if esPrimo and (clave == "calificaciones"):
                print(f"promedio: {promedio}")
        
        #if (n.get("nombre")) == "Luis":
         #   print(f'{clave} : {valor}')
          #  if clave == "calificaciones":
           #     print(f"promedio: {promedio}")