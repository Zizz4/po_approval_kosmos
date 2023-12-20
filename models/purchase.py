from odoo import fields, models, api


class Purchase(models.Model):
    _inherit = 'purchase.order'

    approver_id = fields.Many2one(string='Approver', comodel_name='res.users', tracking=True)
    signature = fields.Binary(string='Signature',
                              help='Attach the signature here')

    def button_confirm(self):
        if self.approver_id:
            self.signature = self.approver_id.ttd
        else:
            approver = self.env.user
            self.approver_id = approver
            self.signature = self.approver_id.ttd
        return super(Purchase, self).button_confirm()

    def button_cancel(self):
        if self.approver_id:
            self.signature = ''
            self.approver_id = ''
        return super(Purchase, self).button_cancel()