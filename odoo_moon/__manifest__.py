# -*- coding: utf-8 -*-

{
    'name': 'Odoo moon',
    
    'summary': """Moon app""",
    
    'description': """
        Moon app to go to the moon:
        [bla]
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/moon_menuitems.xml',
    ],
    
    'demo': [
        'demo/moon_demo.xml',
    ],
    
    'license': 'LGPL-3',
}
