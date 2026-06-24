from fastapi import FastAPI
from model import Product


app=FastAPI()

@app.get("/")
def greeting():
    return "Welcome"

products =[
    Product(name="phone",id=1,description="Flag-ship model",price=32000.27,quantity=27),
    Product(name="car",id=2,description="off street car",price=2000000,quantity=10),
    Product(name="watch",id=6,description="smart watch with 'ai'",price=100000,quantity=50)
]

@app.get("/product")
def get_all_product():
    return products

@app.get("/specific_product")
def get_specific_products(id: int):   
    for product in products:
        if product.id == id:
            return product
        
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

# @app.put("/product")
# def update_product(id: int,name: str):
#     for product in products:
#         if product.id == id:                       """to change name"""
#             product.name = name
#             return product

# @app.put("/product")
# def update_product(id: int,put_product: Product):
#     for product in products:
#         if product.id == id:                       """what mistake i doo? here!"""
#             product= put_product
#             return product

@app.put("/product")
def update_product(id: int,put_product: Product):
    for i in range(len(products)):
        if products[i].id == id:                            #to change change the whole updated products
            products[i]= put_product
            return "added successfully"

        
@app.delete("/products")
def delete_product(id: int,product: Product):
    for product in products:
        if product.id == id:
            products.remove(product)
            return "product detail removed"