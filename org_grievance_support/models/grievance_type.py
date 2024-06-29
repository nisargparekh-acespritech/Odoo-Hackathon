# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GrievanceType(models.Model):
    _name = 'grievance.type'
    _description = 'Grievance Type'

    name = fields.Char(string="Name", required=True)
