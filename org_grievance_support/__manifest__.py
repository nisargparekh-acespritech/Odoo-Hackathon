# -*- coding: utf-8 -*-
{
    'name': "org_grievance_support",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Module regarding Organisation Grievance Support
    """,

    'author': "Team Code Crackers [NHYD]",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'website','portal','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/org_grievance_groups.xml',
        'data/mail_template.xml',
        'data/ir_sequence.xml',
        'data/grievance_type.xml',
        'views/templates.xml',
        'views/my_portal_extension.xml',
        'views/templates.xml',
        'views/employee_grievance_views.xml',
        'views/grievance_type_views.xml',
        'views/dashboard_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/org_grievance_support/static/src/js/dashboard.js',
            '/org_grievance_support/static/src/css/dashboard.css',
            '/org_grievance_support/static/src/xml/dashboard.xml',
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js'
    ]},
}
