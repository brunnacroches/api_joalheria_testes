from controller.products_equivalent_controller import ProductEquivalentController

class ActionViewEquivalent:
    def view_equivalent(self, request):
        body = request.json
        payment = body["payment"]

        action_controller_equivalent = ProductEquivalentController()
        action_controller_equivalent.get_product_equivalent(payment)

        return {
            "status_code": 200,
            "data": {
                "payment": payment,
            },
            "success": True
        }
