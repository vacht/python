#simon sanchez  A00405272
#Entradas

nota1=float(input("Ingrese su nota del parcial 1"))
nota2=float(input("Ingrese su nota del parcial 2"))
nota3=float(input("Ingrese su nota del parcial 3"))
nota4=float(input("Ingrese su nota del examen practico 1"))
nota5=float(input("Ingrese su notar del examen practico 2"))
nota6=float(input("Ingrese su nota del componente gamificado"))
nota7=float(input("Ingrese su nota del proyecto final"))

promedio_individual=(float(nota1+nota2+nota3+nota4+nota5)/5)
print(f"su nota individual es: {promedio_individual}")
promedio_ponderado=(float(nota1*0.1+nota2*0.15+nota3*0.25+nota4*0.075+nota5*0.075+nota6*0.25+nota7*0.1))
print(f"su nota ponderada es: {promedio_ponderado}")

#Salidas 


if promedio_individual < 3:
    print(f"Usted perdio la materia, su nota final es: {promedio_individual}")
elif promedio_ponderado < 3:
    print(f"Usted perdio la materia, su nota final es: {promedio_ponderado}")
else:
    print(f"Usted ganó la materia, su nota final es: {promedio_ponderado}")