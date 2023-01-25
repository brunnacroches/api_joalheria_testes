from action_joalheria import ActionJoalheriaController


class ActionComprarController(ActionJoalheriaController):
    def comprar(self, pagamento: float):
        for produto, price_range in self.produtos.items():
            if price_range[0] <= pagamento <= price_range[1]:
                return produto
        return None

joalheria = ActionJoalheriaController()

