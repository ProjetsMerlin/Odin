from odoo import models, fields

class Website(models.Model):
    _inherit = "website"

    about_text = fields.Html("Texte d’introduction")