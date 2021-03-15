import random

def busqueda_binaria(lista, comienzo, final, objetivo,iter_bin=0,locationid=[]):
    iter_bin +=1
    if comienzo > final:
        return (False,iter_bin,locationid)
    
    medio = (comienzo + final) //2 # division de enteros significa la doble barra //

    if lista[medio] == objetivo:
        locationid.append(1)
        return (True,iter_bin,locationid)
    elif lista[medio] < objetivo:
        locationid.append(1)
        return busqueda_binaria(lista, medio +1, final , objetivo,iter_bin=iter_bin,locationid=locationid)
    else:
        locationid.append(0)
        return busqueda_binaria(lista, comienzo, medio -1, objetivo,iter_bin=iter_bin,locationid=locationid)


if __name__ == '__main__':

    tamano_lista = int(input('Ingrese tamano de lsita '))
    objetivo = int(input('Que numero desea encontrar '))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])

    print(lista)


    encontrado,iter_bin,locationid = busqueda_binaria(lista, 0, len(lista) , objetivo)

    print(f'Encontrado: {encontrado}')
    print(f'En {iter_bin} iteraciones')

    print(locationid)
    suma = 0
    potencia = len(locationid)-1
    for i in locationid:
        suma += i * (2**potencia)
        potencia -=1
    if encontrado:
        print(f'En la posicion {suma} y segun python {lista.index(objetivo)}')
         


