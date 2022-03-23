# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError
from odoo.odoo.fields import Datetime


# class Inventory(models.Model):
#     _name = 'scms.inventory'
#     _description = 'scms.inventory'
#
#     device_id = fields.Many2one('scms.device',string="Device ID", required=True)
#     quantity = fields.Integer(string="Quantity", required=True)

class Device(models.Model):
    _name = 'scms.device'
    _description = 'scms.device'
    _order = 'id desc'

    name = fields.Char(string="Device Name", required=True)
    model = fields.Char(string="Device Model", required=True)
    device_code = fields.Char(string="Device Code", required=True)
    unit = fields.Char(string="Unit", required=True)
    category = fields.Many2one('scms.dev_category',string="Category", required=True)
    supplier = fields.Many2one('scms.suppliers', string="Supplier", required=True)
    price = fields.Char(string="Price", required=True)
    status = fields.Selection([('active','Active'),('idle','Idling'),('broken','Broken')],
                              required=True)

class Device_Category(models.Model):
    _name = "scms.dev_category"
    _order = "id desc"

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description", required=True)