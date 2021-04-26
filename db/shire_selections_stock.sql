DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_details VARCHAR(255),
    info VARCHAR(255)
);

CREATE TABLE products (
    id serial PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT,
    manufacturer_id INT REFERENCES manufacturers(id)
);