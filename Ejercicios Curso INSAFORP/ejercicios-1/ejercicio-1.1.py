# ejercicio a) Que diferencia hay en % entre el curso actual 1.5h y el mas rapido, el promedio y el mas lento de los otros cursos
print("Ejercicio a) el curso de dalto dura: ")
curso_dalto = 1.5
curso_rapido = 2.5
curso_promedio = 4.0
curso_lento = 7.0

diferencia_rapido = 100 - curso_dalto / curso_rapido * 100
diferencia_promedio = 100 - curso_dalto / curso_promedio * 100
diferencia_lento = 100 - curso_dalto / curso_lento * 100

print(f" - un {diferencia_rapido}% menos que el mas rapido")
print(f" - un {diferencia_promedio}% menos que el promedio")
# round redondea el decimal al numero que yo quiera
print(f" - un {round(diferencia_lento,2)}% menos que el mas lento")

# ejercicio b) porcentaje de material inservible que se reduce en este curso y el promedio de los otros cursos
print("\n Ejercicio b) El curso a reducido: ")

crudo_dalto = 3.5
dalto_reducido = 1.5
crudo_otros = 5.0
otros_reducido = 4.0

diferencia_redu_dalto = 100 - dalto_reducido / crudo_dalto * 100
diferencia_redu_otros = 100 - otros_reducido / crudo_otros * 100

print(f" - el de datlto un {round(diferencia_redu_dalto,2)}% el video en crudo")
print(f" - el promedio un {round(diferencia_redu_otros,2)}% el video en crudo")

# ejercicio c) ver 10 horas de este curso es equivalente a ver cuantas horas de otros cursos y al reves, ver 10 horas de otros cursos equivalente a cuantas horas de este curso
print("\n Ejercicio c) ver 10 horas de:")

print(f" - un curso de dalto equivale a ver {round(curso_promedio/curso_dalto*10,2)} de otros cursos promedio")
print(f" - un curso promedio equivale a ver {round(curso_dalto/curso_promedio*10,2)} del curso de dalto")