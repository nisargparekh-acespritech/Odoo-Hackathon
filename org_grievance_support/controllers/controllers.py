# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class OrgGrievanceSupport(http.Controller):

    @http.route('/grievance/registration', type='http', auth='public', website=True)
    def document_upload(self, **kw):
        return request.render("org_grievance_support.my_controller_form")

    @http.route('/my_controller/Submit', type='http', auth="public", website=True)
    def submit_doc(self, **post):
        name = post.get('name')
        email = post.get('email')
        print("\n\n\n-----name",name)
        print("\n\n\n-----email",email)

        grievance_id = request.env['employee.grievance'].sudo().create({
            'employee_id':post.get('employee_id') if post.get('employee_id') else False,
            'grievance_type_id':post.get('grievance_type') if post.get('grievance_type') else False,
            'department_id':post.get('department') if post.get('department') else False,
            'description':post.get('description') if post.get('description') else False,
            'severity':post.get('severity') if post.get('severity') else False,
            'document_id':attachment.id if attachment else False,

        })
        value = {'grievance_id':grievance_id}
        return request.render("org_grievance_support.RegisterMessage",value)
