import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Audio Unity Group", "contact@audio-unity-group.com", "vinyl press")
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer("Push Print", "hello@pushprint.net", "printing")
manufacturer_repository.save(manufacturer_2)


product_1 = Product("Axor - High St. EP [SS004]", "Vinyl EP", 300, 850.50, 10, manufacturer_1.id)
product_repository.save(product_1)

product_2 = Product("SS Logo", "Sticker", 1000, 280.50, 1.00, manufacturer_2.id)
product_repository.save(product_2)



pdb.set_trace()
