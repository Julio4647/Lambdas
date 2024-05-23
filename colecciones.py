# Lista

nombres = ["Lisa", "Mariana", "Sandra", "Veronica"]

for nombre in nombres:
    print(f"Los nombres son: {nombre}")

print(f"nombre de un indice: {nombres[1]}")


#Modificar los elementos de la lista

numeros = [100,200,300,400,500,600]

print(numeros)

numero_a_buscar = 200

indice = numeros.index(numero_a_buscar)

print(f'El indice del numero {numero_a_buscar} es: {indice}')


# Redefinir la lista
numeros = [100, 200, 300, 400, 500]

# Recuperar una sublista. lista[indice_inicio:indice_final - 1]
valores_recuperados = numeros[0: 3] # Se recupera: [0:2]
#print(valores_recuperados)

# Recuperar una sublista indica indice final
valores_recuperados = numeros[:2]
#print(valores_recuperados)

# Recuperar una sublista indicando el indice de inicio
valores_recuperados = numeros[3:]
#print(valores_recuperados)

# Realizar una copia
lista_copiada = numeros[:]
#numeros[0] = 1000 # Son listas distintas en memoria
#print(f'Lista original: {numeros}')
#print(f'Lista copiada: {lista_copiada}')

# Metodos de listas
largo_lista = len(numeros)
#print(f'Largo lista: {largo_lista}')

# Agregar un nuevo elemento. append. Agrega el nuevo elemento al final
numeros.append(600)
#print(f'Lista con el nuevo valor: {numeros}')

# Insertar nuevos elementos, en el indice deseado
numeros.insert(2, 50)
#print(f'LIsta con el nuevo valor: {numeros}')

# Eliminar un valor de una lista
numeros.remove(600)
#print(f'Lista con elemento eliminado: {numeros}')

# Concatenar listar
nueva_lista = numeros + lista_copiada
#print(f'Lista concatenada: {nueva_lista}')

# Eliminar un elemento por indice
del numeros[3]  # removemos por indice
#print(f'Lista sin el valor del indice 3: {numeros}')

# Eliminar la lista completa
numeros[:] = []
#print(f'Lista numeros vacia: {numeros}')

# Eliminar por completo la variable
del numeros
#print(numeros)