# -*- coding: utf-8 -*-
from odoo import fields, models


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    # Ref: https://github.com/odoo/enterprise/blob/14.0/hr_appraisal/models/hr_employee_public.py

    online_appointment_url = fields.Char(
        string='Online appointment URL',
        help='The URL used to be sent to the attendee when he books an online appointment.\n'
             'This can be used to send unique online URL\'s per employee (e.g Hangouts, Zoom, MS teams,.. )'
    )
