from typing import List
from products_controller import ProductsController

class AllowedProductController:
    def __init__(self):
        self.products_controller = ProductsController
        # ! acessando e integrando as informações coletadas da classe
        # ! ProductController onde o sistema foi criado

    def get_allowed_products(self, price:int) -> List[str]:
        return self.products_controller.get_allowed_products(price)
