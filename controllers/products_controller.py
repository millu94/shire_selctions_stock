from flask import Blueprint, Flask, redirect, render_template, request

from models.manufacturer import Manufacturer
from models.product import Product

from repositories.manufacturer_repository as manufacturer_repository