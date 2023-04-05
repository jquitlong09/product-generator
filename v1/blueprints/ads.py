from flask import Blueprint, request
from v1.helpers.validator import Validator
from v1.helpers.openapi import OpenAPI
import v1.helpers.command_template as CT

ads = Blueprint('ads', __name__)
validate = Validator()
openapi = OpenAPI()


@ads.route('/ads', methods=['POST'])
def advertisement():
    required = ["product_description", "vibe_words"]
    response = {}
    try:
        body = request.get_json()
        if validate.validate_required(required, body) is False:
            return "Missing Required Details", 400
        product_names = openapi.get_product_names(body)
        response["product_names"] = product_names
        response["tv_ad_young_adults"] = openapi.get_one_add(
            product_names[0], body["product_description"], CT.TV_AD)
        response["facebook_ad_parents"] = openapi.get_one_add(
            product_names[1], body["product_description"], CT.FB_AD)
        response["radio_ad_parents"] = openapi.get_one_add(
            product_names[1], body["product_description"], CT.RD_AD)
        response["safety_warning"] = openapi.get_one_add(
            ",".join(product_names), "", CT.SF_WR)
    except Exception as e:
        return e, 400
    return response, 201
