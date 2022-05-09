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
    
    'depends': ['project'],
    
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/moon_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml',
        'views/project_mission_inherit.xml',
        'wizard/project_wizard.xml',
        'reports/spaceship_report_template',
    ],
    
    'demo': [
        'demo/moon_demo.xml',
    ],
    
    'license': 'LGPL-3',
}
