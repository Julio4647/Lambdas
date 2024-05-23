name = input('Cual es tu nombre: ')
last_name = input('Cual es tu apellido: ')
name_2 = name.lower()
last_name_2 = last_name.lower()
dominio = '@ciudadgotica.com'

email = f'{name_2}.{last_name_2}{dominio}'

print(f'Tu nuevo correo generado por es sistema es: \n {email} \n *** Felicidades ***')