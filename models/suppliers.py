# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError

class Supplier(models.Model):
    _name = 'scms.suppliers'
    _description = 'scms.suppliers'
    order = 'id desc'

    name = fields.Char(string="Company Name", required=True)
    reg_no = fields.Char(string="Registration Number", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number", required=True)
    fax_no = fields.Char(string="Fax Number")
    website = fields.Char(string="Website")
    address = fields.Text(string="Address", required=True)

    @api.onchange('phone', 'fax_no')
    def _onchange_validate_number(self):
        if self.phone:
            if not self.phone.strip().isdigit() or len(self.phone) != 10:
                self.phone = ''
                return {'warning': {'title': 'Invalid input', 'message': 'Please enter 10 digits Phone number'}}

        if self.fax_no:
            if not self.fax_no.strip().isdigit() or len(self.fax_no) != 10:
                self.fax_no = ''
                return {'warning': {'title': 'Invalid input', 'message': 'Please enter 10 digits Fax number'}}