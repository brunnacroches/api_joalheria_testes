from controller.products_equivalent_controller import ProductEquivalentController

# ! Teste de Sucesso 01
def test_get_product_equivalent_success_01():
    product_equivalent_controller = ProductEquivalentController()

    # Test case 1: success
    result = product_equivalent_controller.get_product_equivalent(10)
    assert result == "Anel", f"Expected 'Anel', but got {result}"

# ! Teste de Sucesso 02
def test_get_product_equivalent__success_02():
    product_equivalent_controller = ProductEquivalentController()

    # Test case 2: success
    result = product_equivalent_controller.get_product_equivalent(70)
    assert result == "Relógio", f"Expected 'Relógio', but got {result}"

# ! Teste de Inválido Input 01
def test_get_product_equivalent_invalid_input_01():
    product_equivalent_controller = ProductEquivalentController()
    # Test case 3: invalid input
    result = product_equivalent_controller.get_product_equivalent(0)
    assert result == "Valor inválido", f"Expected 'Valor inválido', but got {result}"

# ! Teste de Inválido Input 02
def test_get_product_equivalent_invalid_input_02():
    product_equivalent_controller = ProductEquivalentController()
    # Test case 4: invalid input
    result = product_equivalent_controller.get_product_equivalent(120)
    assert result == "Valor inválido", f"Expected 'Valor inválido', but got {result}"
