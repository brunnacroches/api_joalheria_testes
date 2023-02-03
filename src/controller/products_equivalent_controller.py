from products_controller import ProductsController

# ! Iniciando a classe dos produtos equivalentes acessado a classe ProductController
class ProductEquivalentController:
    def __init__(self):
        self.products_controller = ProductsController()
    
    # ! criando a função que define o tipo pagamento e o valor acessando
    # ! o método get_product da classe de ProductController onde 
    # ! fica a lógica da média de preço dos produtos
    def get_product_equivalent(self, payment: int) -> str:
        return self.products_controller.get_product(payment)
