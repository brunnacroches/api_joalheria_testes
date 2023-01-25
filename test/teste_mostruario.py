from src.controller import action_joalheria


# Testes unitários
def test_success():
    entrada = 10.0
    response = action_joalheria(entrada)

    assert isinstance(response, str) == True
    assert response == "Anel"

def test_success_2():
    entrada = 40.0
    response = action_joalheria(entrada)

    assert isinstance(response, str) == True
    assert response == "Pulseira"

def teste_mostrar(entrada):

    if not isinstance(entrada, float):
        raise Exception('Entrada deve ser em float!')

    saida = None
    if 1 <= entrada < 20: saida = "Anel"
    elif 20 <= entrada <= 40: saida = "Anel, Pulseira"
    elif 40 <= entrada <= 60: saida = "Anel, Pulseira, Tiara"
    elif 60 <= entrada <= 100: saida = "Anel, Pulseira, Tiara, Relógio"
    else:
        raise Exception('Error')

    return saida

def test_entrada_not_float():
    entrada = "EntradaErrada"

    try:
        action_joalheria(entrada)
        assert False
    except Exception as exception:
        assert str(exception) == "Entrada deve ser em float!"

def test_entrada_not_in_range():
    entrada = 12.0

    try:
        action_joalheria(entrada)
        assert False
    except Exception as exception:
        assert str(exception) == "Entrada deve ser entre 1 - 20"
