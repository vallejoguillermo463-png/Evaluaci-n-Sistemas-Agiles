# 📚 Sistema de Registro de Estudiantes

## 📖 Descripción

Este proyecto consiste en un sistema desarrollado en Python para registrar y administrar estudiantes junto con sus calificaciones.

El sistema permite validar los datos ingresados, calcular la suma de las calificaciones, determinar el estado académico del estudiante y consultar la información registrada.

Durante el desarrollo del proyecto se aplicaron técnicas de refactorización, organización del código, pruebas unitarias y control de versiones mediante Git y GitHub.

---

## 🎯 Objetivos

- Registrar estudiantes con sus calificaciones.
- Validar la información ingresada.
- Calcular automáticamente la suma de las notas.
- Determinar el estado académico del estudiante.
- Mantener un código limpio y fácil de mantener.
- Aplicar buenas prácticas de desarrollo de software.

---

## ⚙️ Funcionalidades

- Registro de estudiantes.
- Validación del nombre.
- Validación de calificaciones.
- Cálculo automático de la suma de notas.
- Clasificación académica:
  - EXCELENTE
  - APROBADO
  - REPROBADO
- Listado de estudiantes registrados.
- Búsqueda de estudiantes.

---

## 📁 Estructura del Proyecto

```
Evaluacion-Sistemas-Agiles/
│
├── gestor_estudiantes.py
├── estudiante.py
├── main.py
├── README.md
├── pytest.ini
├── .gitignore
│
└── tests/
    └── test_main.py
```

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Pytest
- Git
- GitHub
- Visual Studio Code

---

## ▶️ Ejecución del proyecto

Ejecutar desde la terminal:

```bash
python main.py
```

---

## ✅ Ejecución de pruebas

Ejecutar desde la terminal:

```bash
pytest
```

---

## 🔄 Refactorizaciones realizadas

Durante el desarrollo del proyecto se realizaron diversas mejoras para obtener un código más limpio y mantenible:

- Renombrado de variables.
- Renombrado de funciones.
- Eliminación de código duplicado.
- Creación de funciones auxiliares.
- Separación de responsabilidades.
- Reorganización del proyecto en módulos.
- Implementación de pruebas unitarias.
- Configuración del proyecto mediante `.gitignore` y `pytest.ini`.

---

## 🚀 Evolución del sistema

Como mejora del sistema se implementó una nueva categoría académica:

| Suma de notas | Estado |
|---------------|---------|
| 28 - 30 | EXCELENTE |
| 24 - 27 | APROBADO |
| Menor a 24 | REPROBADO |

Esta modificación demuestra que el sistema puede evolucionar fácilmente gracias a la organización y refactorización del código.

---

## 👨‍💻 Autor

Guillermo Vallejo

Asignatura: Sistemas Ágiles

Evaluación de Refactorización y Diseño Orientado al Cambio.