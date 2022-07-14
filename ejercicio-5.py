# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

a=int(input( "ingrese el total de horas trabajadas: "))
b=int(input( "ingrese el coste por hora G$: "))
c= a * b
print(f"la paga que le corresponde es G$: {c}")