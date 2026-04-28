# Calculadora en Python

Proyecto simple de calculadora en consola.

## Requisitos

- Python 3.10 o superior

## Instalar requerimientos

```bash
py -m pip install -r requirements.txt
```

## Ejecutar

```bash
py -m app.main
```

## Pruebas

Ejecutar pruebas normales:

```bash
py -m pytest
```

Generar reporte HTML:

```bash
py -m pytest --html=report.html --self-contained-html
```


## Estructura

- `app/main.py`: punto de entrada.
- `app/`: código de la aplicación.
- `app/calculator.py`: lógica de operaciones.
- `app/cli.py`: interacción por consola.
