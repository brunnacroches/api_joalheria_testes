from products_controller import ProductsController

# ! Teste de Sucesso 01
def test_get_product_success_01():
  products_controller = ProductsController()

  # Test case 1: success
  result = products_controller.get_product(10)
  assert result == "Anel", f"Expected 'Anel', but got {result}"


# ! Teste de Sucesso 02
def test_get_product_success_02():
  products_controller = ProductsController()

  # Test case 2: success
  result = products_controller.get_product(70)
  assert result == "Relógio", f"Expected 'Relógio', but got {result}"


# ! Teste de Inválido Input 01
def test_get_product_invalid_input_01():
  products_controller = ProductsController()

  # Test case 3: invalid input
  result = products_controller.get_product(0)
  assert result == "Valor inválido", f"Expected 'Valor inválido', but got {result}"


# ! Teste de Inválido Input 02
def test_get_product_invalid_input_02():
  products_controller = ProductsController()

  # Test case 4: invalid input
  result = products_controller.get_product(120)
  assert result == "Valor inválido", f"Expected 'Valor inválido', but got {result}"

  
# ! Teste de Sucesso 01
def test_get_allowed_products_success_01():
  products_controller = ProductsController()

  # Test case 1: success
  result = products_controller.get_allowed_products(30)
  expected = ["Pulseira", "Tiara"]
  assert result == expected, f"Expected {expected}, but got {result}"


# ! Teste de Sucesso 02
def test_get_allowed_products_success_02():
  products_controller = ProductsController()

  # Test case 2: success
  result = products_controller.get_allowed_products(80)
  expected = ["Relógio"]
  assert result == expected, f"Expected {expected}, but got {result}"


# ! Teste de Inválido Input 01
def test_get_allowed_products_invalid_input_01():
  products_controller = ProductsController()

  # Test case 3: invalid input
  result = products_controller.get_allowed_products(0)
  expected = []
  assert result == expected, f"Expected {expected}, but got {result}"


# ! Teste de Inválido Input 02
def test_get_allowed_products_invalid_input_01():
  products_controller = ProductsController()

  # Test case 4: invalid input
  result = products_controller.get_allowed_products(120)
  expected = []
  assert result == expected, f"Expected {expected}, but got {result}"
