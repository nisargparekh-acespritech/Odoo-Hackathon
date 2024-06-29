# -*- coding: utf-8 -*-
from odoo import http,_
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager as portal_pager

class OrgGrievanceSupport(http.Controller):

    @http.route('/grievance/portal', type='http', auth='public', website=True)
    def document_upload(self, **kw):
        return request.render("org_grievance_support.my_controller_form")

    @http.route('/submit_data', type='http', auth="public", website=True)
    def submit_grievance_data(self, **post):
        document_ids = []
        if 'document' in request.httprequest.files:
            documents = request.httprequest.files.getlist('document')
            for document in documents:
                attachment = request.env['ir.attachment'].create({
                    'name': document.filename,
                    'datas': document.read(),
                    'type': 'binary',
                    'res_model': 'employee.grievance',  # Replace with the model where you want to attach the document
                    'res_id': request.env.user.id,  # Replace with the relevant record ID
                })
                document_ids.append(attachment.id)
        print('\n\n\n\n\n documents',document_ids)
        grievance_id = request.env['employee.grievance'].sudo().create({
            'employee_id':post.get('employee_id') if post.get('employee_id') else False,
            'grievance_type_id':post.get('grievance_type') if post.get('grievance_type') else False,
            'department_id':post.get('department') if post.get('department') else False,
            'description':post.get('description') if post.get('description') else False,
            'severity':post.get('severity') if post.get('severity') else False,
            'document_ids':document_ids if document_ids else False,

        })
        value = {'grievance_id':grievance_id}
        return request.render("org_grievance_support.RegisterMessage",value)

    @http.route('/grievance/count', auth='public', type='json')
    def get_grievance_count(self):
        grievance_ids = request.env['employee.grievance'].search([])
        grievance_counts = {
            'pending': 0,
            'on_going': 0,
            'resolved': 0
        }

        for grievance in grievance_ids:
            if grievance.status in grievance_counts:
                grievance_counts[grievance.status] += 1

        grievance_state = ['Pending', 'On Going', 'Resolved']
        total_grievance = [
            grievance_counts['pending'],
            grievance_counts['on_going'],
            grievance_counts['resolved']
        ]
        colors = ['#F0FFFF', '#ADD8E6', '#87CEFA']

        return {
            'grievance': grievance_state,
            'total': total_grievance,
            'color': colors
        }

    @http.route('/grievance/bar', auth='public', type='json')
    def get_bar_graph(self):
        grievance_ids = request.env['employee.grievance'].search([])
        grievance_counts = {
            'pending': 0,
            'on_going': 0,
            'resolved': 0
        }

        for grievance in grievance_ids:
            if grievance.status in grievance_counts:
                grievance_counts[grievance.status] += 1

        total_count = [
            grievance_counts['pending'],
            grievance_counts['on_going'],
            grievance_counts['resolved']
        ]
        state = ['Pending', 'On Going', 'Resolved']

        return [total_count, state]

    @http.route('/grievance/datacount', auth='public', type='json')
    def get_job_order_details(self):
        grievance_ids = request.env['employee.grievance'].search([])
        pending_count = len(grievance_ids.filtered(lambda x:x.status == 'pending'))
        ongoing_count = len(grievance_ids.filtered(lambda x:x.status == 'on_going'))
        resolved_count = len(grievance_ids.filtered(lambda x:x.status == 'resolved'))
        return {
            'pending_count': pending_count,
            'ongoing_count': ongoing_count,
            'resolved_count': resolved_count,
        }

    @http.route(['/my/grievance', '/my/grievance/page/<int:page>'], type='http', auth="user", website=True)
    def show_grievance_records(self,**post):
        employee_grievance = request.env['employee.grievance']
        values = {}

        records = employee_grievance.sudo().search([])
        values.update({
            'records': records,
        })

        return request.render("org_grievance_support.portal_my_grievances",values)
