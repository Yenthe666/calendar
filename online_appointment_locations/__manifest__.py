# -*- coding: utf-8 -*-
{
    'name': "Online appointment locations",

    'summary': """
        Allows setting/configuring a location per employee instead of per appointment type
    """,

    'description': """
        Allows setting/configuring a location per employee instead of per appointment type
    """,

    'author': "Mainframe Monkey",
    'website': "http://www.mainframemonkey.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'hr',
        'website_calendar'
    ],

    # always loaded
    'data': [
        'views/hr_employee_view.xml',
        'views/calendar_type_view.xml',
    ],
}
