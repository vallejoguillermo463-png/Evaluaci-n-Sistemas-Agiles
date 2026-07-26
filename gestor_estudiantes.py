def validar_nota(nota):
    if nota < 0 or nota > 10:
        print("Nota incorrecta")
        return False
    return True