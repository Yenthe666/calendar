# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    online_appointment_url = fields.Char(
        string='Online appointment URL',
        help='The URL used to be sent to the attendee when he books an online appointment.\n'
             'This can be used to send unique online URL\'s per employee (e.g Hangouts, Zoom, MS teams,.. )'
    )
