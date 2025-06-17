from odoo import fields,models

class sparePart(models.Model):
    _name = "sparepart_sparepart"
    _description="this is fondamantal class of this module"
    name= fields.Char("Name", required=True,)
    reference_code= fields.Char()
    description= fields.Text("Description")
    tag_ids = fields.Many2many(
        comodel_name="sparepart_tag",
        string="Tags",
    )
    image_url= fields.Char()
    quantity= fields.Integer()
    location= fields.Char()
    minimal_quantity= fields.Integer()
    selling_price= fields.Integer("Selling Price")
    def action_create_sparepart(self):
        print("Create Sparepart button clicked")