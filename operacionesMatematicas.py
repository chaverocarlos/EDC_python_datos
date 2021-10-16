nombres = input("¿Cuál es tu nombre(s)? ")
nombres = nombres[0:2]
apellidoPaterno = input("¿Cuál es tu apellido paterno? ")
apellidoPaterno = apellidoPaterno[0:1]
apellidoMaterno = input("¿Cuál es tu apellido materno? ")
apellidoMaterno = apellidoMaterno[0:1]
fechaNacimiento = input("¿Cuál es tu fecha de nacimiento? (ejemplo: AAMMDD) ")
print(f"Tu RFC es: {nombres.upper()}{apellidoPaterno.upper()}{apellidoMaterno.upper()}{fechaNacimiento}")