from odoo import models,fields

class tag(models.Model):
    _name = "sparepart_tag"
    _description = "this is tag class of this module"
    
    name = fields.Char("Name", required=True)