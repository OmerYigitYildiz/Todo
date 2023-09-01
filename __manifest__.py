# -*- coding: utf-8 -*-
{
    'name': "To.Do",
    'summary': "To.Do List",
    'author': "Omer Yigit Yildiz",
    'website': "https://kitayazilim.com/",
    'version': '0.1',
    'depends': ['mail'],
    "category": "Services/To.Do",
    "application": True,
    'data': [
        "security/todo_security.xml",
        'security/ir.model.access.csv',
        "views/todo.xml",
        "views/menu.xml",
    ],
}
