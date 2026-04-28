from app.calculator import add, divide, multiply, subtract


def _read_number(prompt: str) -> float:
    # Lee un número desde la consola.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Escribí un número.")


def run() -> None:
    # Muestra un menú simple para usar la calculadora.
    print("Calculadora simple")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")

    valid_options = {"1", "2", "3", "4"}
    option = input("Elegí una opción (1-4): ").strip()
    while option not in valid_options:
        print("Opción inválida. Elegí un número del 1 al 4.")
        option = input("Elegí una opción (1-4): ").strip()

    first = _read_number("Primer número: ")
    second = _read_number("Segundo número: ")

    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
    }

    operation = operations.get(option)
    try:
        result = operation(first, second)
        print(f"Resultado: {result}")
    except ValueError as error:
        print(f"Error: {error}")
