# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EmployeeGrievance(models.Model):
    _name = 'employee.grievance'
    _description = 'Employee Grievance'
    _rec_name = "employee_id"

    name = fields.Char(string="Name")
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
        ('pending', 'Pending'), ('on_going', 'On Going'), ('resolved', 'Resolved')
    ], string="Status",default="pending",
        help="Grievance Status")
    document_id = fields.Many2one('ir.attachment',string='Document')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = 'GRP/' + self.env['ir.sequence'].next_by_code(
                   'grievance.reference')
        res = super().create(vals_list)
        return res

    def send_notification(self,status):
        """
        Send a notification email to the approver when the grievance status changes.

        This method retrieves the mail template for employee notifications, prepares the email values
        with the current status, company email, and approver's name, and then sends the email.

        Parameters:
        status (str): The new status of the grievance.

        Returns:
        None
        """

        mail_template_id = self.env.ref("org_grievance_support.employee_notification_mail_template")
        email_values = {'status': status,'email_from':self.env.company.email,'user':self.approver_id.name}
        mail_template_id.with_context(email_values).sudo().send_mail(self.id, force_send=True)


    def on_going_grievance(self):
        """
        Transition the grievance status to 'on_going'.

        This method changes the status of the grievance to 'on_going'
        if the current status is 'pending'.
        """
        if self.status == 'pending':
            self.status = 'on_going'
            self.send_notification('On Going')

    def resolve_grievance(self):
        """
        Transition the grievance status to 'resolved'.

        This method changes the status of the grievance to 'resolved'
        if the current status is 'on_going'.
        """
        if self.status == 'on_going':
            self.status = 'resolved'
            self.send_notification('Resolved')
