# -*- coding: utf-8 -*-
from odoo.addons.portal.controllers.portal import CustomerPortal


class CalendarResponsible(CustomerPortal):
    def _prepare_calendar_values(self, appointment_type, date_start, date_end, description, name, employee, partner):
        """
            Overrides the default _prepare_calendar_values() from Odoo to inject an unique appointment URL from the
            employee if the employee has one set.
        """
        result = super(CustomerPortal, self)._prepare_calendar_values(
            appointment_type, date_start, date_end, description, name, employee, partner
        )
        if employee.sudo().online_appointment_url:
            result['location'] = employee.sudo().online_appointment_url
        return result
