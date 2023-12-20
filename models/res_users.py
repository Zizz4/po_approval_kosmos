from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    ttd = fields.Binary(string='TTD',
                              help='Attach the signature here')
