from odoo import models,fields

class tag(models.Model):
    _name = "sparepart_tag"
    _description = "this is tag class of this module"
    
    name = fields.Char("Name", required=True,)
    tag_type= fields.Selection(selection=[
        ("manufacturing country", "Manufacturing Country"),
        ("manufacturer", "Manufacturer"),
        ("category", "Category"),
        ("brand", "Brand"),
        ("model", "Model"),
        ("type", "Type"),
        ("size", "Size"),
        ("color", "Color"),
        ("material", "Material"),
        ("condition", "Condition"),
        ("other", "Other")
    ],required=True, string="Tag type")
    def create(self, vals):
        if 'name' in vals and vals['name']:
            vals['name'] = vals['name'].lower()
        return super().create(vals)
    def write(self, vals):
        if 'name' in vals and vals['name']:
            vals['name'] = vals['name'].lower()
        return super().write(vals)