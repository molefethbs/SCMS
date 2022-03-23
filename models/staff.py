from odoo import models, fields, api


class Staff(models.Model):
    _name = "scms.staff"
    _description = "scms.staff"
    order = "id desc"

    name = fields.Char(string="First Name", required=True)
    surname = fields.Char(string="Last Name", required=True)
    address = fields.Text(string="Address", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    email = fields.Char(string="Email", required=True)
    password = fields.Char(string="Password", required=True)
    role = fields.Many2one('scms.roles', string="Role", required=True)

    @api.onchange('phone')
    def _onchange_validate_number(self):
        if self.phone:
            if not self.phone.strip().isdigit() or len(self.phone) != 10:
                self.phone = ''
                return {'warning': {'title': 'Invalid input', 'message': 'Please enter 10 digits Phone number'}}

    @api.onchange('email')
    def onchange_validate_email(self):
        if self.email:
            # rematch_email = re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", self.email,re.IGNORECASE)
            # if rematch_email != None:
            if '@' not in self.email:
                self.email = self.email
                return {'warning': {'title': 'Invalid input', 'message': 'Please enter a valid email address'}}


class Roles(models.Model):
    _name = 'scms.roles'
    _description = 'scms.roles'

    name = fields.Char(string="Role Name", required=True)
    description = fields.Text(string="Access Rights")
