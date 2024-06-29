# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EmployeeGrievance(models.Model):
    _name = 'employee.grievance'
    _description = 'Employee Grievance'
    _rec_name = "employee_id"

    employee_id = fields.Many2one(
        "hr.employee", string="Employee", required=True)
    grievance_type_id = fields.Many2one(
        "grievance.type", string="Grievance Type", required=True)
    department_id = fields.Many2one(
        "hr.department", string="Department", required=True)
    approver_id = fields.Many2one(
        "hr.employee", string="Approver")
    approver_user_id = fields.Many2one(
        "res.users",related="approver_id.user_id")
    description = fields.Text(string="Description", required=True)
    severity = fields.Selection([
        ('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')
    ], string="Severity",
        required=True,
        help="Priority of the grievance")
    status = fields.Selection([
        ('pending', 'Pending'), ('on_going', 'On Going'), ('resolved', 'Resolved')], string="Status",default="pending",
        help="Grievance Status")
    document_id = fields.Many2one('ir.attachment',string='Document')


    def on_going_grievance(self):
        if self.status == 'pending':
            self.status = 'on_going'

    def resolve_grievance(self):
        if self.status == 'on_going':
            self.status = 'resolved'
