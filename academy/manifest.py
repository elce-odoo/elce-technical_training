# -*- coding: utf-8 -*-

{
    'name': 'Odoo moon',
    
    'summary': """Academy app""",
    
    'description': """
        Academy sfgfgk:
        [bla]
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['project'],
    
    'data': [
        'security/security.xml',
        'security/ir.model_menuitems.xml',
        'views/academy_menuitems.xml',
        'views/academy_course.xml',
        'views/academy_session.xml',
        'views/sales_views_inherit',
        'views/academy_product_template',
    ],
    
    'demo': [
        'demo/academy_demo.xml'
    ],
    
    'license': 'LGPL-3',
}
