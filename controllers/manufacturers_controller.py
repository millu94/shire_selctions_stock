from flask import Blueprint, Flask, redirect, render_template, request

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

#index
@manufacturers_blueprint.route("/manufacturer_info")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturer_info/index.html", manufacturers=manufacturers)