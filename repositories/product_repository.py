from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (name, description, quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) Returning *"
    values = [product.name, product.description, product.quantity, product.buying_cost, product.selling_price, product.manufacturer_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for result in results:
        manufacturer = manufacturer_repository.select(result["manufacturer_id"])
        product = Product(result["name"], result["description"], result["quantity"], result["buying_cost"], result["selling_price"], manufacturer, result["id"])
        products.append(product)
    return products

def select(id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    manufacturer = manufacturer_repository.select(result["manufacturer_id"])
    product = Product(result["name"], result["description"], result["quantity"], result["buying_cost"], result["selling_price"], manufacturer, result["id"])
    return product

def update(product):
    sql = "UPDATE products SET (name, description, quantity, buying_cost, selling_price, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.quantity, product.buying_cost, product.selling_price, product.manufacturer_id.id, product.id]
    print(values)
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)