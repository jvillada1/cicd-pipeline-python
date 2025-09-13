# app/calculadora.py

def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Returns:
        float | int: La suma de a y b.
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Returns:
        float | int: La resta de a menos b.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Returns:
        float | int: El producto de a y b.
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float | int): Dividendo.
        b (float | int): Divisor.

    Raises:
        ZeroDivisionError: Si b es 0.

    Returns:
        float: El cociente de a dividido entre b.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
