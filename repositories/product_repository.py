from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository

def save(product):
    sql = "INSERT INTO products (name, description, quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) Returning *"
    values = [product.name, product.description, product.quantity, product.buying_cost, product.selling_price, product.manufacturer_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)