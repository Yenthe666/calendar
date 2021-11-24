# -*- coding: utf-8 -*-
from odoo import http, _, fields
from odoo.addons.website_calendar.controllers.main import WebsiteCalendar


class CalendarResponsible(WebsiteCalendar):
    def _prepare_calendar_values(self, appointment_type, date_start, date_end, description, name, employee, partner):
        """
            Overrides the default _prepare_calendar_values() from Odoo to inject an unique appointment URL from the
            employee if the employee has one set.
        """
        result = super(CalendarResponsible, self)._prepare_calendar_values(
            appointment_type, date_start, date_end, description, name, employee, partner
        )
        if employee.online_appointment_url:
            result['location'] = employee.online_appointment_url
        return result
