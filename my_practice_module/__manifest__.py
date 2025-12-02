# -*- coding: utf-8 -*-
{
    'name': 'My Practice Module',
    'version': '17.0.1.0.0',
    'category': 'Practice',
    'summary': 'A simple module to practice Odoo development',
    'description': """
My Practice Module
==================
This module is designed for practicing basic Odoo development concepts:
- Creating models
- Defining fields
- Building views (tree, form)
- Setting up menus and actions
- Managing security and access rights
    """,
    'author': 'Practice Developer',
    'website': 'https://github.com/Artcrafterrra/odoo-practice',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/practice_task_views.xml',
        'views/practice_menu.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
