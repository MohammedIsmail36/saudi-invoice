# -*- coding: utf-8 -*-
{
    'name': "Saudi Electronic Invoice",
    'summary': 'Saudi Electronic Invoice',
    'description': """
        print Saudi electronic invoice
    """,

    'author': "Mohamed Ahmed Ismail",
    'website': "http://www.mohamedismail.net",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '15.0.1',
    # any module necessary for this one to work correctly
    'depends': ['account','manage_address'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_view.xml',
        'views/account_move_report_action.xml',
        # 'views/templates.xml',
        'report/tax_invoice_report_template.xml',
        'report/simple_tax_invoice_report_template.xml',
        # Actions Report
        'report/report_actions.xml',

        'data/send_email_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_common': [
            # 'saudi_einvoice/static/src/css/style.css',
        ],
    },
    'images': [],

    'installable': True,
    'auto_install': False,
    'application': True,
}
