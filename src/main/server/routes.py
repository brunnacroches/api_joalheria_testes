from flask import jsonify, request
from views.action_view_products import ActionViewProducts
from views.action_view_equivalent import ActionViewEquivalent
from views.action_view_allowed import AllowedProductController

from .server import app

# ! POST PARA CRIAR UM NOVO RECURSO
@app.route("/rota1/products", methods=["POST"])
def route_products():
    action_view_products = ActionViewProducts()

    http_response = action_view_products.view_products(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

# ! POST PARA CRIAR UM NOVO RECURSO ou
# ! PATCH PARA ATUALIZAR PARCIALMENTE UM RECURSO EXISTENTE
@app.route("/rota1/equivalent", methods=["POST"])
def route_equivalent():
    action_view_equivalent = ActionViewEquivalent()

    http_response = action_view_equivalent.view_equivalent(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

# ! POST PARA CRIAR UM NOVO RECURSO ou
# ! PATCH PARA ATUALIZAR PARCIALMENTE UM RECURSO EXISTENTE
@app.route("/rota1/allowed", methods=["POST"])
def route_allowed():
    action_view_allowed = AllowedProductController()

    http_response = action_view_allowed.get_allowed_products(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

