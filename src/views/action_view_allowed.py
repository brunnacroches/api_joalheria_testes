from controller.products_allowed_products_controller import AllowedProductController

class ActionViewAllowed:
    def view_allowed(self, request):
        body = request.json
        price = body.price

        action_controller_allowed = AllowedProductController()
        action_controller_allowed.get_allowed_products(price)

        return {
            "status_code": 200,
            "data": {
                "price": price,
            },
            "success": True
        }
