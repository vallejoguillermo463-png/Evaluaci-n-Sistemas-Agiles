estudiantes = []
NOTA_MINIMA_APROBACION = 24

def validar_nota(nota):
    if nota < 0 or nota > 10:
        print("Nota incorrecta")
        return False
    return True

def validar_nombre(nombre):
    if nombre.strip() == "":
        print("Nombre incorrecto")
        return False
    return True

def calcular_suma(nota1, nota2, nota3):
    return nota1 + nota2 + nota3

def determinar_estado(suma):
    if suma >= NOTA_MINIMA_APROBACION:
        return "APROBADO"
    return "REPROBADO"

def registrar_estudiante(nombre, nota1, nota2, nota3):
    if not validar_nombre(nombre):
        return

    if not validar_nota(nota1):
        return

    if not validar_nota(nota2):
        return

    if not validar_nota(nota3):
        return

    suma = calcular_suma(nota1, nota2, nota3)

    estado = determinar_estado(suma)

    estudiantes.append({
        "nombre": nombre,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "suma": suma,
        "estado": estado
    })

    print("Estudiante registrado")

def listar_estudiantes():
    if len(estudiantes) == 0:
        print("No existen estudiantes")
    else:
        print("LISTA DE ESTUDIANTES")
        for e in estudiantes:
            print(
                e["nombre"],
                e["nota1"],
                e["nota2"],
                e["nota3"],
                e["suma"],
                e["estado"]
            )

def buscar_estudiante(nombre):
    encontrado = False

    for e in estudiantes:
        if e["nombre"] == nombre:
            print(
                e["nombre"],
                e["nota1"],
                e["nota2"],
                e["nota3"],
                e["suma"],
                e["estado"]
            )
            encontrado = True

    if encontrado == False:
        print("Estudiante no encontrado")
