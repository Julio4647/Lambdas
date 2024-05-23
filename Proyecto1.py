import random

name = input('Cual es tu Nombre: ')
last_name = input('Cual es tu apellido: ')
birthday = input('Cual es tu Año de Nacimiento: ')

name_upper = name.upper()
last_name_upper = last_name.upper()

first_position = name_upper[0:2]
second_position = last_name_upper[0:2]
third_position = birthday[2:4]
number_random = random.randint(1000,9999)

person_id = first_position + second_position + third_position

print(f'Hola {name}, habitante de ciudad gotica! \n Tu nuevo numero de identificacion (ID) generado por el sistema es: \n {person_id}{number_random} \n Felicidades!')