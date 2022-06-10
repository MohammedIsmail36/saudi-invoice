# -*- coding: utf-8 -*-
{
    'name': "Manage Address",

    'summary': """
        Manage Address Add City And district""",

    'description': """
       Manage Address Add City And district
    """,

    'author': "Mohammed Ahmed Ismail",
    'website': "http://www.mohamedismail.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/res.country.state.csv',
        'data/address.cities.csv',
        'data/address.districts.csv',
        'views/views.xml',
        'views/cities_view.xml',
        'views/districts_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
