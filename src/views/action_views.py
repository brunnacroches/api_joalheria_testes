from controller.action_comprar import ActionComprarController
from controller.action_joalheria import ActionJoalheriaController
from controller.action_mostrar import ActionMostruarioController


class ActionViewJoalheria:
    def view_joalheria(sef, request):
        body = request.json
        user_agent = request.headers["User-Agent"]

        action_controller_joalheria = ActionJoalheriaController()
        body_validation = action_controller_joalheria.action(body)

        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }



class ActionViewComprar:
    def view_comprar(self, request):
        body = request.json
        user_agent = request.headers["User-Agent"]

        action_controller_comprar = ActionComprarController()
        body_validation = action_controller_comprar.action(body)

        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }


class ActionViewMostruario:
    def view_mostruario(self, request):
        body = request.json
        user_agent = request.headers["User-Agent"]

        action_controller_mostrar = ActionMostruarioController()
        body_validation = action_controller_mostrar.action(body)

        return {
            "status_code": 200,
            "data": {
                "validation": body_validation,
                "userAgent": user_agent
            },
            "success": True
        }
