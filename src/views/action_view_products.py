from controller.products_controller import ProductsController


class ActionViewProducts:
    def view_products(sef, request):
        body = request.json
        payment = body.payment

        action_controller_products = ProductsController()
        action_controller_products.get_product(payment)

        return {
            "status_code": 200,
            "data": {
                "payment": payment
            },
            "success": True
        }
