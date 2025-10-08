# from odoo import http
# from odoo.http import request

# class OdinWebsite(http.Controller):

#     @http.route(['/odin', '/odin/<string:slugPage>'], type='http', auth='public', website=True)
#     def odin_page(self, slugPage=None, **kw):
#         return request.render('odin.odin_home')