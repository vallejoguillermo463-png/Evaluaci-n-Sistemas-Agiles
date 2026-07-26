from gestor_estudiantes import (
    validar_nota,
    calcular_suma,
    determinar_estado,
    obtener_estudiantes,
    registrar_estudiante,
)


def test_validar_nota_correcta():
    assert validar_nota(8) is True


def test_validar_nota_limite():
    assert validar_nota(10) is True


def test_validar_nota_incorrecta():
    assert validar_nota(12) is False


def test_calcular_suma():
    assert calcular_suma(8, 8, 8) == 24


def test_estado_excelente():
    assert determinar_estado(29) == "EXCELENTE"


def test_estado_aprobado():
    assert determinar_estado(24) == "APROBADO"


def test_estado_reprobado():
    assert determinar_estado(18) == "REPROBADO"


def test_registrar_estudiante():
    obtener_estudiantes().clear()

    registrar_estudiante("Pedro", 10, 9, 10)

    estudiantes = obtener_estudiantes()

    assert len(estudiantes) == 1
    assert estudiantes[0]["nombre"] == "Pedro"
    assert estudiantes[0]["estado"] == "EXCELENTE"


def test_registrar_estudiante_invalido():
    obtener_estudiantes().clear()

    registrar_estudiante("", 8, 8, 8)

    assert len(obtener_estudiantes()) == 0