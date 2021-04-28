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

#new product
@products_blueprint.route("/add_product")
def add_item():
    manufacturers = manufacturer_repository.select_all()
    return render_template("inventory/add_product.html", manufacturers=manufacturers)

#create product
@products_blueprint.route("/add_product", methods=["POST"])
def add_products():
    name = request.form["name"]
    description = request.form["description"]
    quantity = request.form["quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    manufacturer_id = request.form["manufacturer"]
    manufacturer = manufacturer_repository.select(manufacturer_id)
    new_products = Product(name, description, quantity, buying_cost, selling_price, manufacturer)
    product_repository.save(new_products)
    return redirect("/inventory")


#edit
@products_blueprint.route("/inventory/<id>/edit")
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("inventory/edit.html", product=product, manufacturers=manufacturers)

#update
@products_blueprint.route("/inventory/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    description = request.form["description"]
    quantity = request.form["quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    manufacturer_id = request.form["manufacturer"]
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, quantity, buying_cost, selling_price, manufacturer, id)
    product_repository.update(product)
    return redirect("/inventory")



#delete
@products_blueprint.route("/inventory/<id>")
def delete_product(id):
    product_repository.delete(id)
    return redirect("/inventory")