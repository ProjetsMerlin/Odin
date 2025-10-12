from odoo import models, fields

class WebsiteParagraphText(models.Model):
    _name = 'website.paragraph.text'
    _description = 'Paragraphe pour la section introduction'

    name = fields.Char(string="Titre", required=True)
    content = fields.Html(string="Contenu")