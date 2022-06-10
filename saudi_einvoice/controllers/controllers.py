# -*- coding: utf-8 -*-
# from odoo import http


# class SaudiEinvoice(http.Controller):
#     @http.route('/saudi_einvoice/saudi_einvoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saudi_einvoice/saudi_einvoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('saudi_einvoice.listing', {
#             'root': '/saudi_einvoice/saudi_einvoice',
#             'objects': http.request.env['saudi_einvoice.saudi_einvoice'].search([]),
#         })

#     @http.route('/saudi_einvoice/saudi_einvoice/objects/<model("saudi_einvoice.saudi_einvoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saudi_einvoice.object', {
#             'object': obj
#         })
