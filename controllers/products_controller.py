from flask import Blueprint, Flask, redirect, render_template, request

from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

#index
@products_blueprint.route("/inventory")
def inventory():
    products = product_repository.select_all()
    return render_template("inventory/index.html", products=products)
