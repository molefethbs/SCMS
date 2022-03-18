# -*- coding: utf-8 -*-
{
    'name': "Supply Chain Management",

    'summary': """
        The module is developed for Supply Chain Management""",

    'description': """
        The module is about the Supply Chain Management System
    """,

    'author': "Molefe Thabiso - molefethbs@gmail.com",
    'category': 'Inventory',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/suppliers_view.xml',
        'views/device_category.xml',
        'views/device.xml',
        'views/menus.xml',
        'views/staff_view.xml',
        'views/roles.xml'
    ],

    "active": False,
    'application': True,
    "sequence": 10
}
