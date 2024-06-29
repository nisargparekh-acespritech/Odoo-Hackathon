# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class org_grievance_support(models.Model):
#     _name = 'org_grievance_support.org_grievance_support'
#     _description = 'org_grievance_support.org_grievance_support'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

