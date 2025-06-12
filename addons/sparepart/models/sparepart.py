from odoo import fields,models

class sparePart(models.Model):
    _name = "sparepart.sparepart"
    _description="this is fondamantal class of this module"
    id: int= fields.Integer("ID",required=True)
    name: str=fields.Char("Name",translate=True, required=True,)
    referece_code:str=fields.Char()
    description: str= fields.Text("description")
    tags: list= fields.Many2many(
        comodel_name="tag",
        relation="sparepart_tags_rel",
        column1="sparepart_id",
        column2="tag_id"
    )
    image_url: str= fields.Char()
    quantity: int= fields.Integer()
    location: str= fields.Char()
    minimal_quantity: int= fields.Integer()