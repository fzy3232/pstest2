# -*- coding: utf-8 -*-
{
   'name': "修改审批",

   'summary': """
    修改审批""",

   'description': """
    False
   """,

   'author': "Einfo-Tech",
   'website': "http://www.einfo-tech.com",
   'category': 'Tools',
   'version': '1.0',

   'depends': ['base','contacts'],

   'data': [
		"views/contact_modify.xml", 
		"views/contact_modify_line.xml", 
		"security/ir.model.access.csv",
 		"security/res.groups.xml",
 		"views/menu.xml",
 		"views/data.xml",
 
   ],

   "installable":True,

}