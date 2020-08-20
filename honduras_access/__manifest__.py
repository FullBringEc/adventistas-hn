# -*- coding: utf-8 -*-
{
    'name': 'Honduras Access Rights',

    'summary': """ Honduras Access Rights """,

    'description': """
        Honduras Access Rights
    """,

    'author': 'Eduwebgroup',
    'website': 'http://www.eduwebgroup.com',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'account',
        'account_asset',
        'point_of_sale',
        'hr_payroll_extends',
    ],

    'data': [
        'data/ir_module_category_data.xml',
        'data/res_groups_data.xml',
        'security/ir.model.access.csv',
        'views/account_menus.xml',
        'views/res_partner_make_sale_views.xml',
        'views/pos_session_views.xml',
        'views/hr_contract_views.xml',
        'views/account_asset_views.xml',
    ],
}