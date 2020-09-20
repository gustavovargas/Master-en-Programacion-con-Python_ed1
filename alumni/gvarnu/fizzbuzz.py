def fizzbuzz(up_to: int):
    output = []
    for number in range(1, up_to + 1):
        representation_tokens = []

        if is_divisible(number, 3):
            representation_tokens.append('fizz')

        if is_divisible(number, 5):
            representation_tokens.append('buzz')

        if not representation_tokens:
            representation_tokens.append(str(number))

        output.append(' '.join(representation_tokens))

    print(', '.join(output))


def is_divisible(number, divisor) -> bool:
    """
    Comprueba la divisibilidad del primer parámetro entre el segundo.

    :param number: el número sobre el que se quiere comprobar la divisibilidad.
    :param divisor: el criterio de divisibilidad.
    :return: True si el primer parámetro es múltiplo del segundo.
    """
    return number % divisor == 0


if __name__ == '__main__':
    fizzbuzz(100)