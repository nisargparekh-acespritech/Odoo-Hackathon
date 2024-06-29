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
    description = fields.Text(string="Description", required=True)
    severity = fields.Selection([
        ('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')
    ], string="Severity",
        required=True,
        help="Priority of the grievance")
    status = fields.Selection([
        ('pending', 'Pending'), ('on_going', 'On Going'), ('resolved', 'Resolved')
    ], string="Status",defualt='pending',
        help="Grievance Status")
    
    document_id = fields.Many2one('ir.attachment',string='Document')
