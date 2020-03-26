# -*- coding: utf-8 -*-
{
    'name': "Honduras Invoices",

    'summary': """ Allow you make honduras invoices """,

    'description': """
        Honduras Invoices and Reports, this add min and max invoice number,
        issue limit date.
    """,

    'author': "EduwebGroup",
    'website': "http://www.eduwebgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.3-beta',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'account_reports', 'school_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_partner_views.xml',
        'views/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
