from controller import products_controller

# Testes unitários

def teste_comprar(entrada):

    if not isinstance(entrada, float):
        raise Exception('Entrada deve ser em float!')

    saida = None
    if 1 <= entrada < 20: saida = "Anel"
    elif 20 <= entrada <= 40: saida = "Pulseira"
    elif 40 <= entrada <= 60: saida = "Tiara"
    elif 60 <= entrada <= 100: saida = "Relógio"
    else:
        raise Exception('Entrada deve ser entre 1 - 100')

    return saida


def test_success():
    entrada = 20.0
    response = products_controller(entrada)

    assert isinstance(response, str) == True
    assert response == "Anel"

def test_success_2():
    entrada = 40.0
    response = products_controller(entrada)

    assert isinstance(response, str) == True
    assert response == "Pulseira"

def test_entrada_not_float():
    entrada = "EntradaErrada"

    try:
        products_controller(entrada)
        assert False
    except Exception as exception:
        assert str(exception) == "Entrada deve ser em float!"

def test_entrada_not_in_range():
    entrada = 12.0

    try:
        products_controller(entrada)
        assert False
    except Exception as exception:
        assert str(exception) == "Entrada deve ser entre 1 - 20"
