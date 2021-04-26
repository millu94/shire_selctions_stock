from flask import Blueprint, Flask, redirect, render_template, request

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

#index
@manufacturers_blueprint.route("/manufacturer_info")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturer_info/index.html", manufacturers=manufacturers)

#create
@manufacturers_blueprint.route("/manufacturer_info", methods=["POST"])
def add_manufacturer():
    name = request.form["name"]
    contact_details = request.form["contact_details"]
    info = request.form["info"]
    new_manufacturer = Manufacturer(name, contact_details, info)
    manufacturer_repository.save(new_manufacturer)
    return redirect("/manufacturer_info")

#edit
@manufacturers_blueprint.route("/manufacturer_info/<id>/edit")
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturer_info/edit.html", manufacturer = manufacturer)

#update
@manufacturers_blueprint.route("/manufacturer_info/<id>", methods=["POST"])
def update_manufacturer(id):
    name = request.form["name"]
    contact_details = request.form["contact_details"]
    info = request.form["info"]
    manu_id = manufacturer_repository.select(id)
    updated_manufacturer = Manufacturer(name, contact_details, info, manu_id.id)
    manufacturer_repository.update(updated_manufacturer)
    return redirect("/manufacturer_info")

#delete
@manufacturers_blueprint.route("/manufacturer_info/<id>")
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturer_info")