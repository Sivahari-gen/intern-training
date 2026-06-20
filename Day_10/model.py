from pydantic import BaseModel

class Product(BaseModel):
    name: str
    id: int
    description: str
    price: float
    quantity: int

    # def __init__(self,name: str, id: int, description: str, price: float, quantity: int):
    #     self.name = name
    #     self.id = id
    #     self.description = description
    #     self.price = price
    #     self.quatity = quantity



    # @app.put("/product")
    # def update_product(id: int,put_product: Product):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i]= put_product
    #         return "added successfully"