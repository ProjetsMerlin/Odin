# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class ContactController(http.Controller):

    @http.route(['/contact/submit'], type='http', auth="public", methods=['POST'], csrf=True, website=True)
    def submit_contact_form(self, **post):
        name = post.get('name')
        email = post.get('email')

       # Vérification minimale
        if not (name and email):
            return request.redirect('/contact')

        # Créer un partenaire
        partner = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email,
        })

        password = generate_password()

        # Créer un utilisateur
        user = request.env['res.users'].sudo().create({
            'name': name,
            'login': email,
            'email': email,
            'password': password,
            'partner_id': partner.id,
            'groups_id': [(6, 0, [request.env.ref('base.group_user').id])],
        })

        return request.render("odin.contact_thank_you")