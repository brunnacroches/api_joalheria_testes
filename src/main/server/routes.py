from flask import jsonify, request
from views.action_views import (ActionViewComprar, ActionViewJoalheria,
                                ActionViewMostruario)

from .server import app


@app.route("/rota1/joalheria", methods=["GET"])
def route_joalheria():
    action_view = ActionViewJoalheria()

    http_response = action_view.view_action(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

@app.route("/rota1/comprar", methods=["GET"])
def route_comprar():
    action_view = ActionViewComprar()

    http_response = action_view.view_action(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

@app.route("/rota1/mostruario", methods=["GET"])
def route_mostruario():
    action_view = ActionViewMostruario()

    http_response = action_view.view_action(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

