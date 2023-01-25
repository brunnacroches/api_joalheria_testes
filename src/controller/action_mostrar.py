from action_joalheria import ActionJoalheriaController


class ActionMostruarioController(ActionJoalheriaController):
    def mostruario(self, preco: float):
        produtos_permitidos = []
        for produto, price_range in self.products.items():
            if price_range[0] <= preco:
                produtos_permitidos.append(produto)
        return produtos_permitidos

joalheria = ActionJoalheriaController()

