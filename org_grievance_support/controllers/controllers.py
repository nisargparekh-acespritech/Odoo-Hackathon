# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class OrgGrievanceSupport(http.Controller):

    @http.route('/my_controller', type='http', auth='public', website=True)
    def document_upload(self, **kw):
        return request.render("org_grievance_support.my_controller_form")

    @http.route('/my_controller/Submit', type='http', auth="public", website=True)
    def submit_doc(self, **post):
        name = post.get('name')
        email = post.get('email')
        print("\n\n\n-----name",name)
        print("\n\n\n-----email",email)
        return request.render("org_grievance_support.RegisterMessage")