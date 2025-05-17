# -*- coding: utf-8 -*-
{
    'name': "hotel",
    'summary': "Hotel Management System",
    'description': "Hotel Guest Registration and Billing System",
    'author': "ROYTEK",
    'website': "https://www.yourcompany.com",
    # Categories can be used to filter modules in module listings
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
   
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mainmenu.xml',
        'views/charges.xml',    
        'views/roomtypes.xml',
        'views/rooms.xml',        
        'views/guests.xml',
        'views/guestregistration.xml',
        # 'views/hoteldocuments.xml',                
    ],
   
    'installable': True,
    'application': True,
}