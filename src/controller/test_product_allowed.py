from products_allowed_products_controller import AllowedProductController


# ! Teste de Sucesso 01
def test_get_allowed_products_sucess_01():
    allowed_product_controller = AllowedProductController()

    # Test case 1: success
    result = allowed_product_controller.get_allowed_products(30)
    expected = ["Pulseira", "Tiara"]
    assert result == expected, f"Expected {expected}, but got {result}"


# ! Teste de Sucesso 02
def test_get_allowed_products_sucess_02():
    allowed_product_controller = AllowedProductController()

    # Test case 2: success
    result = allowed_product_controller.get_allowed_products(80)
    expected = ["Relógio"]
    assert result == expected, f"Expected {expected}, but got {result}"


# ! Teste de Inválido Input 01
def test_get_allowed_products_invalid_input_01():
    allowed_product_controller = AllowedProductController()

    # Test case 3: invalid input
    result = allowed_product_controller.get_allowed_products(0)
    expected = []
    assert result == expected, f"Expected {expected}, but got {result}"


# ! Teste de Inválido Input 02
def test_get_allowed_products_invalid_input_02():
    allowed_product_controller = AllowedProductController()

    # Test case 4: invalid input
    result = allowed_product_controller.get_allowed_products(120)
    expected = []
    assert result == expected, f"Expected {expected}, but got {result}"
