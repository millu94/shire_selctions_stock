from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product


def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, address, info) VALUES (%s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.contact_details, manufacturer.info]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)