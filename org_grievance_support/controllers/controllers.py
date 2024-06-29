# -*- coding: utf-8 -*-
# from odoo import http


# class OrgGrievanceSupport(http.Controller):
#     @http.route('/org_grievance_support/org_grievance_support', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/org_grievance_support/org_grievance_support/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('org_grievance_support.listing', {
#             'root': '/org_grievance_support/org_grievance_support',
#             'objects': http.request.env['org_grievance_support.org_grievance_support'].search([]),
#         })

#     @http.route('/org_grievance_support/org_grievance_support/objects/<model("org_grievance_support.org_grievance_support"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('org_grievance_support.object', {
#             'object': obj
#         })

