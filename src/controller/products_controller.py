from typing import List, Tuple

# ! Definindo a classe com os nomes dos produtos, preço mínimo, e o preço máximo 
# ! Cadastro de produtos
class Product:
    def __init__(self, name:str, min_price: int, max_price: int):
        self.name = name
        self.min_price = min_price
        self.max_price = max_price

# ! Controle de produtos e definindo o valor mínimo e o valor máximo
class ProductsController:
    def __init__(self):
        self.products = [
            Product("Anel", 1, 20),
            Product("Pulseira", 20, 40),
            Product("Tiara", 40, 60),
            Product("Relógio", 60, 100)
        ]
    # ! Verificação se o preço confere com o preço estabelecido acima
    def get_product(self, payment: int) -> str:
        for product in self.product:
            if payment >= product.min_price and payment <= product.max_price:
                return product.name
            return "Valor inválido"

    # ! Adicionando em uma lista com método append os produtos que estão dentro
    def get_allowed_product(self, price:int) -> List[str]:
        allowed = []
        for product in self.products:
            if price >= product.min_price and price <= product.max_price:
                allowed.append(product.name)
        return allowed
