from odoo import models

class sparePart(models.Model):
    _name: str = "sparepart"
    id: int
    name: str
    description: str
    tags: list
    image_url: str
    quantity: int
    location: str
    minimal_quantity: int
    buy_price: int
    sell_price: int