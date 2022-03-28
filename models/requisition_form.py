from odoo import models, fields, api


class RequisitionForm(models.Model):
    _name = 'scms.user_requisition'
    _description = 'scms.user_requisition'

    name = fields.Many2one('scms.staff',string="Name", required=True)
    department = fields.Many2one('scms.roles', string="Department", required=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    delivery_location = fields.Text(string="Delivery Location", required=True)