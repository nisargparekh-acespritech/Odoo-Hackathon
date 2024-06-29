# -*- coding: utf-8 -*-

from odoo import models, fields, api


class org_grievance_support(models.Model):
    _name = 'org_grievance_support'
    _description = 'org_grievance_support'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()

    def action_channel_enroll(self):
    	return {
            'type': 'ir.actions.act_url',
            'url': '/my_controller',
            'target': 'self',
        }
