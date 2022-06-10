# -*- coding: utf-8 -*-
# from odoo import http


# class ManageAddress(http.Controller):
#     @http.route('/manage_address/manage_address', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manage_address/manage_address/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manage_address.listing', {
#             'root': '/manage_address/manage_address',
#             'objects': http.request.env['manage_address.manage_address'].search([]),
#         })

#     @http.route('/manage_address/manage_address/objects/<model("manage_address.manage_address"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manage_address.object', {
#             'object': obj
#         })
