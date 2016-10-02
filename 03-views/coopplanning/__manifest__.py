# -*- coding: utf-8 -*-
{
    'name': "Coop Task Management",

    'summary': """
        Volonteer Timetable Management""",

    'description': """

    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Coop',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        "views/task_template.xml",
        "views/task.xml",
        "views/configuration.xml", #File for extra 03
        "data/coopplanning_data.xml",
        "data/task_template_demo.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
}
