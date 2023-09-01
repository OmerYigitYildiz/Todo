from odoo import api, fields, models


class Todo(models.Model):
    _name = "to.do"
    _description = "To.Do"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    stacktrace = fields.Text(required=True)
    is_ok = fields.Boolean()
