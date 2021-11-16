# -*- coding: utf-8 -*-
{
    'name': "Custom Leaves LSF",

    'summary': """
        Leaves As Per lsf""",

    'description': """
        Leaves As Per lsf
    """,

    'author': "Xero1 LTD",
    'website': "http://www.xeroone.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'employees',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr','calendar','hr_holidays'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}