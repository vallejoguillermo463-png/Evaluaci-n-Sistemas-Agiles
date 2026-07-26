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



